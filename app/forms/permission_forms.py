from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from extensions import db
from app.models.permission import Permission


class PermissionCreateForm(FlaskForm):
    name = StringField(
        "Permission Name",
        validators=[DataRequired(), Length(max=120)],
    )

    code = StringField(
        "Permission Code",
        validators=[DataRequired(), Length(max=120)],
    )

    module = StringField(
        "Module",
        validators=[DataRequired(), Length(max=80)],
    )

    description = TextAreaField(
        "Description",
        validators=[Length(max=255)],
    )

    submit = SubmitField("Create")

    def validate_code(self, field):
        exists = db.session.scalar(
            db.select(Permission).filter(Permission.code == field.data)
        )
        if exists:
            raise ValidationError("This permission code already exists.")


class PermissionEditForm(FlaskForm):
    name = StringField(
        "Permission Name",
        validators=[DataRequired(), Length(max=120)],
    )

    code = StringField(
        "Permission Code",
        validators=[DataRequired(), Length(max=120)],
    )

    module = StringField(
        "Module",
        validators=[DataRequired(), Length(max=80)],
    )

    description = TextAreaField(
        "Description",
        validators=[Length(max=255)],
    )

    submit = SubmitField("Save Changes")

    def __init__(self, original_permission: Permission, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_permission = original_permission

    def validate_code(self, field):
        exists = db.session.scalar(
            db.select(Permission).filter(
                Permission.code == field.data,
                Permission.id != self.original_permission.id
            )
        )
        if exists:
            raise ValidationError("This permission code already exists.")


# --------------------------
# FIX: Delete confirmation
# --------------------------
class ConfirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")
