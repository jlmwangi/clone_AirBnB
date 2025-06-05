#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes class state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns cities"""
            from models import storage
            cities_val = models.storage.all(City).values()
            cities_list = []
            for city in cities_val:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
