#!/usr/bin/python3
'''serializes instances to a JSON file and deserializes JSON file to instances'''

import json


class FileStorage:
    '''where the serializing and deserializing happens'''
    __file_path = 'file.json'
    __objects = {}  # <class name>.id


    def all(self):
        '''returns the dictionary _objects'''
        return self.__objects

    def new(self, obj):
        '''sets in objects the obj with the key <obj class name>.id'''
        key = f"{obj.__class__.__name__}.{obj.id}"

        # set in objects the value
        self.__objects[key] = obj

    def save(self):
        '''serializes/save/encode, to a json format, objects to the json file(__file_path)'''
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        '''deserializes the json file to __objects
        Remove from a json format to an object'''
        try:
            with open(self.__file_path, "r") as json_file:
                data = json.load(json_file)

                from models.base_model import BaseModel
                from models.user import User
                from models.place import Place
                from models.state import State
                from models.city import State
                from models.review import Review
                from models.amenity import Amenity

                for key, value in data.items():
                    # separate the key into class name and obj id which was set earlier
                    class_name, obj_id = key.split('.')

                    if class_name == 'BaseModel':
                        # dynamically get the class
                        cls = BaseModel
                    elif class_name == 'User':
                        cls = User
                    elif class_name == 'Place':
                        cls = Place
                    elif class_name == 'State':
                        cls = State
                    elif class_name == 'City':
                        cls = City
                    elif class_name == 'Review':
                        cls = Review
                    elif class_name == 'Amenity':
                        cls = Amenity
                    else:
                        pass

                    # create an object from an instance of class using the dictionary
                    obj = cls(**value)
                    self.__objects[key] = obj


        except FileNotFoundError:
            pass

