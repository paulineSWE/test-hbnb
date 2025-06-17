# models/review.py
from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not text:
            raise ValueError("Text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        if not place or not user:
            raise ValueError("Both place and user must be provided.")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
