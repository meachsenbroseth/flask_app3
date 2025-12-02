from typing import List, Optional
from app.models.permission import Permission
from extensions import db

class PermissionService:
    @staticmethod
    def get_all() -> List[Permission]:
        return Permission.query.order_by(Permission.id.desc()).all()

    @staticmethod
    def get_by_id(permission_id: int) -> Optional[Permission]:
        return Permission.query.get(permission_id)

    @staticmethod
    def create(data: dict) -> Permission:
        permission = Permission(
            name=data["name"],
            code=data["code"],
            module=data.get("module"),
        )

        db.session.add(permission)
        db.session.commit()
        return permission

    @staticmethod
    def update(permission: Permission, data: dict) -> Permission:
        permission.name = data["name"]
        permission.code = data["code"]
        permission.module = data.get("module")

        db.session.commit()
        return permission

    @staticmethod
    def delete(permission: Permission) -> None:
        db.session.delete(permission)
        db.session.commit()
