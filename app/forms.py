from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField(
        "Name",
        validators=[
            DataRequired(),
            Length(min=3, max=20)
        ]
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )
    confirm_password = PasswordField(
        "Password Confirmation",
        validators=[
            DataRequired(),
            EqualTo("password")
        ]
    )
    submit = SubmitField("Register")