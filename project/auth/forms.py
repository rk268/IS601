from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo, Length, Optional

class RegisterForm(FlaskForm):
    #rk268 5/2/23
    FIRSTNAME = StringField("FIRSTNAME", validators=[DataRequired(), Length(2, 30)])
    LASTNAME =  StringField("LASTNAME", validators=[DataRequired(), Length(2, 30)])
    username = StringField("username", validators=[DataRequired(), Length(2, 30)])
    email = EmailField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("confirm", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    #rk268 5/2/23
    email = StringField("email or username", validators=[DataRequired()]) #EmailField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[InputRequired()])
    submit = SubmitField("Login")

class ProfileForm(FlaskForm):
    #rk268 5/2/23
    username = StringField("username", validators=[DataRequired(), Length(2, 30)])
    FIRSTNAME = StringField("FIRSTNAME", validators=[DataRequired(), Length(2, 30)])
    LASTNAME =  StringField("LASTNAME", validators=[DataRequired(), Length(2, 30)])
    email = EmailField("email", validators=[DataRequired(), Email()])
    current_password = PasswordField("current password", validators=[Optional()])
    password = PasswordField("password", validators=[Optional(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("confirm", validators=[Optional(), EqualTo("password")])
    submit = SubmitField("Update")