from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"}
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password"}
    )

    submit = SubmitField("Login")
class RegistrationForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"}
    )
    username = StringField(
        "Username",
        validators=[DataRequired()],
        render_kw={"placeholder": "Username"}
    )
    full_name = StringField(
        "Full Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Full Name"}
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password"}
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Confirm Password"}
    )

    submit = SubmitField("Register")