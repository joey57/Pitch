from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
  email = StringField('Your Email Address', validators=[DataRequired(),Email()])
  username = StringField('Enter your username', validators= [DataRequired()])
  password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
  submit = SubmitField('Sign up')

  def validate_email(self,data_field):
    if User.query.filter_by(email=data_field.data).first():
     raise ValidationErr('There is an account with that email')
   

  def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationErr('That username is taken')
