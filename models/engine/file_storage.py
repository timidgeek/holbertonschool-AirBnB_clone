#!/usr/bin/python3
"""The class FileStorage serializes instances to a JSON file and
deserializes JSON for to instances"""
import json
import models
from models.base_model import User



class FileStorage:
    """initalizes FileStorage"""
    __file__path = "file.json"
    __objects = {}

    @classmethod
    def all(self):
        """returns dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objexts the obk with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        jsonobj = {}
        for k, v in self.__objects.items():
            jsonobj = v.to_dict()
        with open(self.__file.path, "w") as fool:
            json.dump(jsonobj, fool)

    def reload(self):
        """deserializes the JSON file to __objexts only if the JSON file
        (__file__path) exists, otherwise do nothing"""
        try:
            with open(self.__file.path, 'r') as fool:
                jenna = json.load(fool)
                for k in jenna:
                    self.__file__path[k] = getattr(models, jenna[k]
                                                   ['__class__'])(**jenna[k])
        except FileNotFoundError:
            pass
