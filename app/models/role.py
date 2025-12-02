from datetime import datetime
from extensions import db
from app.models.associations import user_roles, role_permissions

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    permissions = db.relationship(
        "Permission",
        secondary=role_permissions,
        back_populates="roles"
    )

    users = db.relationship(
        "User",
        secondary="user_roles",
        back_populates="roles"
    )

    def __repr__(self):
        return f"<Role {self.name}>"
