#!/usr/bin/python3
"""A class called user that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
