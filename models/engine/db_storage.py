#!/usr/bin/python3
"""defines a new engine"""

import os
import models
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classnames = {
        'State': State,
        'Place': Place,
        'City': City,
        'Amenity': Amenity,
        'User': User,
        'Review': Review
        }


class DBStorage:
    """instantiates a class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the class"""
        mysql_user = os.getenv("HBNB_MYSQL_USER")
        mysql_pwd = os.getenv("HBNB_MYSQL_PWD")
        mysql_host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        mysql_db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(mysql_user, mysql_pwd,
                                        mysql_host, mysql_db),
                                       pool_pre_ping=True)

        self.metadata = MetaData()
        self.metadata.bind = self.__engine

        hbnb_env = os.getenv("HBNB_ENV")
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """queries current database section for all objects"""
        if not self.__session:
            self.reload()

        objs = {}
        if isinstance(cls, str):
            cls = classnames.get(cls, None)

        if cls:
            for obj in self.__session.query(cls):
                objs[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for cls in classnames.values():
                for obj in self.__session.query(cls):
                    objs[f"{obj.__class__.__name__}.{obj.id}"] = obj

        return objs

    def new(self, obj):
        """add object to current database section"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from current session if obj is not none"""
        if not self.__session:
            self.reload()
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """removes the private session"""
        if self.__session:
            self.__session.remove()

    def get(self, cls, id):
        ''' A method to retrieve one object'''
        if cls not in classnames.values():
            return None

        objects = models.storage.all(cls)
        for obj in objects.values():
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        ''' count number of objects in storage'''
        if cls is None:
            objects = models.storage.all()
        else:
            objects = models.storage.all(cls)

        return len(objects)
