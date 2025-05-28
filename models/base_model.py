#!/usr/bin/python3
"""Holds a class that defines all common attributes and methods for other classes"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """defines all common attributes and methods"""
    def __init__(self, *args, **kwargs):
        """initialize public instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                # convert created at and updated at strings to datetime objexts
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))

                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

            storage.new(self)

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates public instance attribute """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """returns a dict containing all key values of dict of the instance"""
        return {
                '__class__': self.__class__.__name__,
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(),
                **{k: v for k,v in self.__dict__.items() if k not in ('created_at', 'updated_at')}
        }
