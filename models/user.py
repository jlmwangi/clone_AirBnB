#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base
import hashlib
import bcrypt


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'users'
        '''__table_args__ = {
                'mysql_charset': 'latin1',
                'mysql_collate': 'latin1_swedish_ci'
        }'''
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user", cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes a user"""
        super().__init__(*args, **kwargs)

        if 'email' in kwargs:
            self.email = kwargs['email']

        if 'password' in kwargs:
            password = kwargs['password']
            password_bytes = password.encode('utf-8')

            hashed_pw = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

            self.password = hashed_pw.decode('utf-8')

        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']

        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
