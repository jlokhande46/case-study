from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

class LoginForm(FlaskForm):
	username=StringField('username',validators=[DataRequired(),Length(min=2, max=20)])
	password=PasswordField('password',validators=[DataRequired()])
	submit = SubmitField('Sign In')