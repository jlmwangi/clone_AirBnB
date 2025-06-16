#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """class that inherits from base model and base"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'amenities'
        '''__table_args__ = {
                'mysql_charset': 'utf8mb4',
                'mysql_collate': 'utf8mb4_0900_ai_ci'
        }'''

        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes amenity"""
        super().__init__(*args, **kwargs)
        if 'name' in kwargs:
            self.name = kwargs['name']
