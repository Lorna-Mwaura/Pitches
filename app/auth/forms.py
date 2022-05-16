from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, length, ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    username = StringField('Enter your username', validators=[DataRequired(), length(min=5, max=20)])
    email = StringField('Your Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Password', validators=[DataRequired() , EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')