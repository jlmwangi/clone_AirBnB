#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes reviews"""
        super().__init__(*args, **kwargs)

        if 'place_id' in kwargs:
            self.place_id = kwargs['place_id']

        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']

        if 'text' in kwargs:
            self.text = kwargs['text']
