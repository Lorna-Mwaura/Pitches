from flask_wtf import FlaskForm


from wtforms.validators import DataRequired,Email
from ..models import User

from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
# from wtforms.validators import 
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
