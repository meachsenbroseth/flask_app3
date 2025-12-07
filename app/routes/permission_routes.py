from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    abort,
)

from app.forms.permission_forms import (
    PermissionCreateForm,
    PermissionEditForm,
    ConfirmDeleteForm
)

from app.services import PermissionService
from flask_login import login_required


permission_bp = Blueprint("permissions", __name__, url_prefix="/permissions")


# -----------------------------
# LIST ALL PERMISSIONS
# -----------------------------
@permission_bp.route("/")
@login_required
def index():
    permissions = PermissionService.get_all()
    return render_template("permissions/index.html", permissions=permissions)


# -----------------------------
# PERMISSION DETAILS
# -----------------------------
@permission_bp.route("/<int:permission_id>")
def detail(permission_id: int):
    permission = PermissionService.get_by_id(permission_id)
    if permission is None:
        abort(404)

    return render_template("permissions/detail.html", permission=permission)


# -----------------------------
# CREATE PERMISSION
# -----------------------------
@permission_bp.route("/create", methods=["GET", "POST"])
def create():
    form = PermissionCreateForm()

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "code": form.code.data,
            "module": form.module.data,
            "description": form.description.data,
        }

        permission = PermissionService.create(data)
        flash(f"Permission '{permission.code}' created successfully.", "success")
        return redirect(url_for("permissions.index"))

    return render_template("permissions/create.html", form=form)


# -----------------------------
# EDIT PERMISSION
# -----------------------------
@permission_bp.route("/<int:permission_id>/edit", methods=["GET", "POST"])
def edit(permission_id: int):
    permission = PermissionService.get_by_id(permission_id)
    if permission is None:
        abort(404)

    form = PermissionEditForm(original_permission=permission, obj=permission)

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "code": form.code.data,
            "module": form.module.data,
            "description": form.description.data,
        }

        PermissionService.update(permission, data)
        flash(f"Permission '{permission.code}' updated successfully.", "success")
        return redirect(url_for("permissions.detail", permission_id=permission.id))

    return render_template("permissions/edit.html", form=form, permission=permission)


# -----------------------------
# DELETE CONFIRMATION
# -----------------------------
@permission_bp.route("/<int:permission_id>/delete", methods=["GET"])
def delete_confirm(permission_id: int):
    permission = PermissionService.get_by_id(permission_id)
    if permission is None:
        abort(404)

    form = ConfirmDeleteForm()
    return render_template("permissions/delete_confirm.html", form=form, permission=permission)


# -----------------------------
# DELETE ACTION
# -----------------------------
@permission_bp.route("/<int:permission_id>/delete", methods=["POST"])
def delete(permission_id: int):
    permission = PermissionService.get_by_id(permission_id)
    if permission is None:
        abort(404)

    PermissionService.delete(permission)
    flash("Permission deleted successfully.", "success")
    return redirect(url_for("permissions.index"))
