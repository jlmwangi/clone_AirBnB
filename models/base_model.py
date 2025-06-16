#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import models

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """A base class for all hbnb models"""

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), unique=True, primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

        for key in ('created_at', 'updated_at'):
            if key in kwargs and isinstance(kwargs[key], str):
                try:
                    setattr(self, key, datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f'))

                except ValueError:
                    setattr(self, key, datetime.strptime(kwargs[key], '%Y-%m-%d %H:%M:%S.%f'))

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dictionary = self.__dict__.copy()
        if "created_at" in new_dictionary:
            new_dictionary["created_at"] = new_dictionary["created_at"].isoformat()
        if "updated_at" in new_dictionary:
            new_dictionary["updated_at"] = new_dictionary["updated_at"].isoformat()
        if 'reviews' in new_dictionary:
            new_dictionary.pop('reviews', None)
        if '_password' in new_dictionary:
            if getenv('HBNB_TYPE_STORAGE') == 'db':
                new_dictionary.pop('_password', None)
            new_dictionary['password'] = new_dictionary['_password']
            #new_dictionary.pop('_password', None)
        if 'amenities' in new_dictionary:
            new_dictionary.pop('amenities', None)
        new_dictionary["__class__"] = self.__class__.__name__
        new_dictionary.pop('_sa_instance_state', None)
        return new_dictionary

    def delete(self):
        """deletes current instance from storage"""
        from models import storage
        models.storage.delete(self)
