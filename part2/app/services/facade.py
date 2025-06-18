from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        # Dépôts dédiés
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()  # Ajout du dépôt pour les amenities

    # ---------- USERS ----------

    def create_user(self, data):
        required_fields = ["first_name", "last_name", "email"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        if "@" not in data["email"]:
            raise ValueError("Invalid email address")

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

    # ---------- AMENITIES ----------

    def create_amenity(self, data):
        if 'name' not in data or not data['name']:
            raise ValueError("Missing required field: name")

        amenity = Amenity(name=data['name'])
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        self.amenity_repo.update(amenity_id, data)
        return self.amenity_repo.get(amenity_id)
