#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns list of objects of one type of class"""
        if cls is None:
            return FileStorage.__objects
        else:
            if not isinstance(cls, type) and not isinstance(cls, tuple):
                raise TypeError
            return {key:obj for key, obj in FileStorage.__objects.items()
                    if isinstance(obj, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes obj from _objects if its inside"""
        if obj is None:
            return
        else:
            del self.__objects[obj.__class__.__name__ + '.' + obj.id]
            self.save()

    def close(self):
        """deserializes  json file objects"""
        self.reload()

    def get(self, cls, id):
        '''retrieve one object'''
        if not cls:
            return None

        for obj in self.__objects.values():
            if isinstance(obj, cls) and obj.id == id:
                return obj

        return None

    def count(self, cls=None):
        '''count number of objects in storage'''
        if not cls:
            objects = self.all()
        else:
            objects = self.all(cls)

        return len(objects)
