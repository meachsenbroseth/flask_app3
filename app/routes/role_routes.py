from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    abort,
)

from app.forms.role_forms import RoleCreateForm, RoleEditForm
from app.forms.user_forms import ConfirmDeleteForm   # You already have this form
from app.models.permission import Permission
from app.services.role_service import RoleService
from flask_login import login_required

role_bp = Blueprint("roles", __name__, url_prefix="/roles")


@role_bp.route("/")
@login_required
def index():
    roles = RoleService.get_all()
    return render_template("roles/index.html", roles=roles)


@role_bp.route("/<int:role_id>")
def detail(role_id: int):
    role = RoleService.get_by_id(role_id)
    if role is None:
        abort(404)
    return render_template("roles/detail.html", role=role)


# @role_bp.route("/create", methods=["GET", "POST"])
# def create():
#     form = RoleCreateForm()

#     # Load permission list
#     all_permissions = Permission.query.all()
#     form.permissions.choices = [(p.id, p.name) for p in all_permissions]
#     permission_map = {p.id: p for p in all_permissions}

#     if form.validate_on_submit():
#         data = {
#             "name": form.name.data,
#             "description": form.description.data,
#             "permissions": form.permissions.data,
#         }
#         role = RoleService.create(data)
#         flash(f"Role '{role.name}' was created successfully.", "success")
#         return redirect(url_for("roles.index"))

#     return render_template("roles/create.html", form=form, permission_map=permission_map)
@role_bp.route("/create", methods=["GET", "POST"])
def create():
    form = RoleCreateForm()

    # Load permission list
    all_permissions = Permission.query.all()
    form.permissions.choices = [(p.id, p.name) for p in all_permissions]
    permission_map = {p.id: p for p in all_permissions}

    # FIX: Prevent NoneType in the template
    if not form.permissions.data:
        form.permissions.data = []

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "description": form.description.data,
            "permissions": form.permissions.data,
        }
        role = RoleService.create(data)
        flash(f"Role '{role.name}' was created successfully.", "success")
        return redirect(url_for("roles.index"))

    return render_template("roles/create.html", form=form, permission_map=permission_map)


# @role_bp.route("/<int:role_id>/edit", methods=["GET", "POST"])
# def edit(role_id: int):
#     role = RoleService.get_by_id(role_id)
#     if role is None:
#         abort(404)

#     form = RoleEditForm(original_role=role, obj=role)

#     # Load permission list
#     all_permissions = Permission.query.all()
#     form.permissions.choices = [(p.id, p.name) for p in all_permissions]
#     form.permissions.data = [p.id for p in role.permissions]
#     permission_map = {p.id: p for p in all_permissions}

#     if form.validate_on_submit():
#         data = {
#             "name": form.name.data,
#             "description": form.description.data,
#             "permissions": form.permissions.data,
#         }
#         RoleService.update(role, data)
#         flash(f"Role '{role.name}' was updated successfully.", "success")
#         return redirect(url_for("roles.detail", role_id=role.id))

#     return render_template("roles/edit.html", form=form, role=role, permission_map=permission_map)
from flask import request

@role_bp.route("/<int:role_id>/edit", methods=["GET", "POST"])
def edit(role_id: int):
    role = RoleService.get_by_id(role_id)
    if role is None:
        abort(404)

    form = RoleEditForm(original_role=role, obj=role)

    # Load permission list
    all_permissions = Permission.query.all()
    form.permissions.choices = [(p.id, p.name) for p in all_permissions]
    permission_map = {p.id: p for p in all_permissions}

    # Only set the defaults on GET
    if request.method == "GET":
        form.permissions.data = [p.id for p in role.permissions]

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "description": form.description.data,
            "permissions": form.permissions.data,  # now returns correct POST values
        }
        RoleService.update(role, data)
        flash(f"Role '{role.name}' was updated successfully.", "success")
        return redirect(url_for("roles.detail", role_id=role.id))

    return render_template(
        "roles/edit.html",
        form=form,
        role=role,
        permission_map=permission_map
    )


@role_bp.route("/<int:role_id>/delete", methods=["GET"])
def delete_confirm(role_id: int):
    role = RoleService.get_by_id(role_id)
    if role is None:
        abort(404)

    form = ConfirmDeleteForm()
    return render_template("roles/delete_confirm.html", role=role, form=form)


@role_bp.route("/<int:role_id>/delete", methods=["POST"])
def delete(role_id: int):
    role = RoleService.get_by_id(role_id)
    if role is None:
        abort(404)

    RoleService.delete(role)
    flash("Role was deleted successfully.", "success")
    return redirect(url_for("roles.index"))
