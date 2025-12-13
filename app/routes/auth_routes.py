from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.forms.auth_forms import LoginForm, RegistrationForm
from app.models.user import User
from extensions import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not user.check_password(form.password.data):
            flash("Invalid email or password.", "danger")
            return redirect(url_for("auth.login"))

        if not user.is_active:
            flash("Your account is inactive.", "warning")
            return redirect(url_for("auth.login"))

        login_user(user)
        flash("Logged in successfully.", "success")

        next_page = request.args.get("next") or url_for("users.index")
        return redirect(next_page)

    return render_template("auth/login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered.", "danger")
            return redirect(url_for("auth.register"))

        new_user = User(
            email=form.email.data,
            username=form.username.data,
            full_name=form.full_name.data
        )
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.login"))
