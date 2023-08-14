#!/usr/bin/python3
"""Classs Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place
Attrs:
    city_id: The city id
    user_id: The user id
    name: The name
    description: The description
    number_rooms : the number of rooms
    number_bathrooms: The number of bathrooms
    max_guest: The max guest number
    price_by_night: The price of a night there
    latitude: the latitude
    longitude: The longitude
    amenity_ids: List of amenity
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
