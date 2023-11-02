#!/usr/bin/python3
from models.base_model import BaseModel
"""
This script defines a BaseModel class for managing and persisting data.
"""


class User(BaseModel):
    """
    Class user that inherits from base model
    """
    email = ""
    pasword = ""
    first_name = ""
    last_name = ""
