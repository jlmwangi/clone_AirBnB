#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    '''__table_args__ = {
            'mysql_charset': 'utf8mb4',
            'mysql_collate': 'utf8mb4_0900_ai_ci'
    }'''

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes class city"""
        super().__init__(*args, **kwargs)
        if 'name' in kwargs:
            self.name = kwargs['name']

        if 'state_id' in kwargs:
            self.state_id = kwargs['state_id']

