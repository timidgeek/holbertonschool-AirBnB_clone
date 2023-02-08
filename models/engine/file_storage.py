#!/usr/bin/python3
"""The class FileStorage serializes instances to a JSON file and
deserializes JSON for to instances"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """initalizes FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """gettin' init, if you will"""
        pass
    
    @classmethod
    def all(self):
        """returns dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        jsonobj = {}
        for k, v in self.__objects.items():
            jsonobj[k] = v.to_dict()
        with open(self.__file_path, "w") as fool:
            json.dump(jsonobj, fool)

    def reload(self):
        """deserializes the JSON file to __objexts only if the JSON file
        (__file__path) exists, otherwise do nothing"""
        try:
            with open(self.__file_path, 'r') as fool:
                jenna = json.load(fool)
                for key, value in jenna.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
