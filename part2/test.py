# test.py
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

# User
user = User("Alice", "Smith", "alice@example.com")
print("User created:", user.to_dict())

# Place
place = Place("Nice house", "By the beach", 120, 45.0, -60.0, user)
user.add_place(place)
print("Place created:", place.to_dict())

# Amenity
wifi = Amenity("Wi-Fi")
place.add_amenity(wifi)
print("Amenity added:", wifi.to_dict())

# Review
review = Review("Very clean and cozy!", 5, place, user)
place.add_review(review)
user.add_review(review)
print("Review created:", review.to_dict())
