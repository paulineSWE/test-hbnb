import uuid
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email, is_admin=False, password=""):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def update(self, data):
        for key, value in data.items():
            if key in ['first_name', 'last_name', 'email', 'is_admin', 'password']:
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<User {self.email} ({'Admin' if self.is_admin else 'User'})>"
    