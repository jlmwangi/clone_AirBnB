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
        __table_args__ = {
                'mysql_charset': 'utf8mb4',
                'mysql_collate': 'utf8mb4_0900_ai_ci'
        }

        name = Column(String(128), unique=True, nullable=False)
        cities = relationship("City", cascade="all, delete", backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes class state"""
        super().__init__(*args, **kwargs)
        if 'name' in kwargs:
            self.name = kwargs['name']

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
