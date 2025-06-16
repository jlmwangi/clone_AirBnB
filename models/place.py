#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Integer, Table, String, Float, ForeignKey
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.amenity import Amenity
from os import getenv
from sqlalchemy.orm import relationship
import os

if getenv("HBNB_TYPE_STORAGE") == 'db':
        place_amenity = Table("place_amenity", Base.metadata,
                              Column('place_id', String(60), ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id', String(60), ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'places'
        '''__table_args__ = {
                'mysql_charset': 'latin1',
                'mysql_collate': 'latin1_swedish_ci'
        }'''
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, default=10, nullable=False)
        number_bathrooms = Column(Integer, default=10, nullable=False)
        max_guest = Column(Integer, default=10, nullable=False)
        price_by_night = Column(Integer, default=10, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False, backref="place_amenities")
    else:
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

    def __init__(self, *args, **kwargs):
        """initializes a place"""
        super().__init__(*args, **kwargs)

        if 'number_rooms' in kwargs:
            self.number_rooms = kwargs['number_rooms']

        if 'number_bathrooms' in kwargs:
            self.number_bathrooms = kwargs['number_bathrooms']

        if 'max_guest' in kwargs:
            self.max_guest = kwargs['max_guest']

        if 'price_by_night' in kwargs:
            self.price_by_night = kwargs['price_by_night']

        if 'city_id' in kwargs:
            self.city_id = kwargs['city_id']

        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']

        if 'name' in kwargs:
            self.name = kwargs['name']

        if 'description' in kwargs:
            self.description = kwargs['description']

        if 'latitude' in kwargs:
            self.latitude = kwargs['latitude']

        if 'longitude' in kwargs:
            self.longitude = kwargs['longitude']

    @property
    def reviews():
        """returns list of review instances"""
        review_values = models.storage.all("Review").values()
        review_list = []
        for review in review_values:
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """returns list of amenity instances"""
            amenities_values = models.storage.all("Amenity").values()
            amenities_list = [amenity for amenity in amenities_values if amenity.place_id == self.id]

            return amenities_list

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)
