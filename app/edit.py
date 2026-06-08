from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import PasswordField
from wtforms import SubmitField

class EditForm(FlaskForm):
    website = StringField(
        "Website",
        validators=[DataRequired()]
    )
    username = StringField(
        "Username",
        validators=[DataRequired()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )
    submit = SubmitField(
        "Update"
    )