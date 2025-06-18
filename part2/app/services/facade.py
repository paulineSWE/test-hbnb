from app.persistence.repository import InMemoryRepository
from app.models.user import User


class HBnBFacade:
    def __init__(self):
        # Un dépôt dédié aux utilisateurs
        self.user_repo = InMemoryRepository()

    def create_user(self, data):
        required_fields = ["first_name", "last_name", "email"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        # Validation email minimale
        if "@" not in data["email"]:
            raise ValueError("Invalid email address")

        # Vérifie unicité de l'email
        existing = self.user_repo.get_by_attribute("email", data["email"])
        if existing:
            raise ValueError("Email already in use")

        user = User(**data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        self.user_repo.update(user_id, data)
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)
