from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'users',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'users',lazy="dynamic")
    
@property
def password(self):
    raise AttributeError('You cannot read the password attribute')

@password.setter
def password(self, password):
    self.pass_secure = generate_password_hash(password)

def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)

class Pitch(db.Model):from flask_login import login_required
    
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    # category = 
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
    # upvote =
    # downvote =


class Comment(db.Model):

    __tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

@login_manager.user_loader
    def load_user(user_id):
    return User.query.get(int(user_id))

def __repr__(self):
        return f'User {self.username}'
