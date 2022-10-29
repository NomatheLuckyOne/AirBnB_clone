#!/usr/bin/python3
"""
Class Review inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class has public attributes
    """
    place_id = ""
    user_id = ""
    text = ""
