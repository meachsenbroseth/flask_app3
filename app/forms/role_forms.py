from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length
from extensions import db
from app.models.role import Role
from app.models.permission import Permission


class RoleCreateForm(FlaskForm):
    name = StringField(
        "Role Name",
        validators=[DataRequired(), Length(min=2, max=80)],
        render_kw={"placeholder": "Enter role name"}
    )

    description = TextAreaField(
        "Description",
        validators=[Length(max=255)],
        render_kw={"placeholder": "Describe this role (optional)"}
    )

    # permissions loaded in route
    permissions = SelectMultipleField(
        "Permissions",
        coerce=int  # permission IDs
    )

    submit = SubmitField("Create")

    # ---- unique role name ----
    def validate_name(self, field):
        exists = db.session.scalar(
            db.select(Role).filter(Role.name == field.data)
        )
        if exists:
            raise ValueError("Role name already exists.")


class RoleEditForm(FlaskForm):
    name = StringField(
        "Role Name",
        validators=[DataRequired(), Length(min=2, max=80)]
    )

    description = TextAreaField(
        "Description",
        validators=[Length(max=255)]
    )

    permissions = SelectMultipleField(
        "Permissions",
        coerce=int
    )

    submit = SubmitField("Save Changes")

    def __init__(self, original_role: Role, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_role = original_role

    def validate_name(self, field):
        exists = db.session.scalar(
            db.select(Role).filter(
                Role.name == field.data,
                Role.id != self.original_role.id
            )
        )
        if exists:
            raise ValueError("Role name already exists.")
