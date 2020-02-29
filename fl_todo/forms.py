from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from flask_wtf import FlaskForm
from .models import User

class UserRegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=16)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
    confirmed = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6, max=30), EqualTo('password', message='The passwords are not the same')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("That username is already taken")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("That email is already taken")

class UserLoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Submit')

class CreateListForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=30)])
    description = StringField('Description')
    submit = SubmitField('Create')

class CreateTaskForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    done = BooleanField('Completed')
    submit = SubmitField('Add')