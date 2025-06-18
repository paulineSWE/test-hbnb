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
        data = self.__dict__.copy()
        data.pop('password', None)
        return data

    def update(self, data):
        for key, value in data.items():
            if key in ['first_name', 'last_name', 'email', 'is_admin', 'password']:
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
