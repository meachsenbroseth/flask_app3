# from typing import List, Optional
# from app.models.role import Role
# from extensions import db

# class RoleService:
#     @staticmethod
#     def get_all() -> List[Role]:
#         return Role.query.order_by(Role.id.desc()).all()

#     @staticmethod
#     def get_by_id(role_id: int) -> Optional[Role]:
#         return Role.query.get(role_id)

#     @staticmethod
#     def create(data: dict) -> Role:
#         role = Role(
#             name=data["name"],
#             description=data.get("description"),
#         )

#         # attach permissions if provided
#         if "permissions" in data:
#             role.permissions = data["permissions"]

#         db.session.add(role)
#         db.session.commit()
#         return role

#     @staticmethod
#     def update(role: Role, data: dict) -> Role:
#         role.name = data["name"]
#         role.description = data.get("description")

#         # update permissions if passed in
#         if "permissions" in data:
#             role.permissions = data["permissions"]

#         db.session.commit()
#         return role

#     @staticmethod
#     def delete(role: Role) -> None:
#         db.session.delete(role)
#         db.session.commit()

from typing import List, Optional
from app.models.role import Role
from app.models.permission import Permission
from extensions import db

class RoleService:
    @staticmethod
    def get_all() -> List[Role]:
        return Role.query.order_by(Role.id.desc()).all()

    @staticmethod
    def get_by_id(role_id: int) -> Optional[Role]:
        return Role.query.get(role_id)

    @staticmethod
    def create(data: dict) -> Role:
        # convert permission IDs → Permission objects
        permission_ids = data.get("permissions", [])
        permissions = Permission.query.filter(Permission.id.in_(permission_ids)).all()

        role = Role(
            name=data["name"],
            description=data.get("description"),
            permissions=permissions
        )

        db.session.add(role)
        db.session.commit()
        return role

    @staticmethod
    def update(role: Role, data: dict) -> Role:
        role.name = data["name"]
        role.description = data.get("description")

        # convert permission IDs → Permission objects
        permission_ids = data.get("permissions", [])
        role.permissions = Permission.query.filter(Permission.id.in_(permission_ids)).all()

        db.session.commit()
        return role

    @staticmethod
    def delete(role: Role) -> None:
        db.session.delete(role)
        db.session.commit()
