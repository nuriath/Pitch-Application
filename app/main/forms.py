 
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us about you.',validators = [Required()])
   submit = SubmitField('Submit')

class PitchForm(FlaskForm):
   description = TextAreaField('Write down here your pitch',validators=[Required()])
   category = StringField('category',validators=[Required()])
   submit = SubmitField('Submit')

class Comment(FlaskForm):
   comment = TextAreaField('Leave you comment here.',validators = [Required()])
   submit = SubmitField('Submit')

class FormVotes(FlaskForm):
   submit = SubmitField('vote')


