#!/usr/bin/python3
"""Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review
Attrs:
    place_id: The place id
    user_id: The user id
    text: the review
    """
    place_id = ""
    user_id = ""
    text = ""
