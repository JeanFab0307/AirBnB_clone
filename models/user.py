#!/usr/bin/python3
"""Class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class
Attrs:
    email: the email
    password: the password
    first_name: The first name
    last_name: The last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

