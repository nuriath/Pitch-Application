from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import  User, Pitch, Comment
from flask_login import login_required
from .forms import PitchForm,UpdateProfile
from .. import db,photos

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The Pitch Application'

    return render_template('index.html', title = title)

@main.route('/incubators/')
def incubators():
    
    Pitch= pitch.Pitch
    title = 'Home - Welcome to The best Pitching Website Online'  
    return render_template('index.html', title = title, pitches= pitches )

@main.route('/business/')
def business():
    
    title = 'Business Pitches'

    pitches= Pitch.pitch

    return render_template('index.html', title = title, pitches= pitches )

@main.route('/education/')
def education():
    
    title = 'Edication Pitches'

    Pitch= pitch.Pitch

    return render_template('index.html', title = title, pitches= pitches )



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.Updatecommit()

    return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
   user = User.query.filter_by(username = uname).first()
   if 'photo' in request.files:
       filename = photos.save(request.files['photo'])
       path = f'photos/{filename}'
       user.profile_pic_path = path
       db.session.commit()
   return redirect(url_for('main.profile',uname=uname))

@main.route('/new', methods=['GET', 'POST'])
@login_required

def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():

        pitch = form.pitch.data
        title = form.title.data
        category = form.category.data
    
        new_pitch = Pitch(pitch=pitch, title=title, category=category, user_id=current_user.id)

       
        new_pitch.save_pitch()
        return redirect(url_for('main.new_pitch'))


        db.session.add(new_pitch)
        db.session.commit()

    return render_template('new_pitch.html',form=pitch_form)

# @main.route('/music/pitch')
# def music(pitch):
    
#     return render_template('index.html')

# @main.route('/edication/')
# def edication():
    
#     return render_template('index.html')

# @main.route('/business/')
# def business():
    
#     return render_template('index.html')