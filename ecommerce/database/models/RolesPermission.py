from ecommerce.database import db


class RolesPermission(db.Model):
    __tablename__ = 'roles_permissions_map'

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),
                          nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'),
                          nullable=False)
    @property
    def __str__(self):
        return self.role_id+'-'+self.permission_id

    def __init__(self, role_id,permission_id):
        self.role_id = role_id
        self.permission_id = permission_id
