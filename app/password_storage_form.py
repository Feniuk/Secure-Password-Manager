from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField


class StorageForm(FlaskForm):
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
        "Save Data"
    )