#!/usr/bin/python3
"""This is the BaseModel for the AirBnB clone project"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This is the base class for all the other classes"""

    def __init__(self, *args, **kwargs):
        """this initalizes the class ~(^-^)~"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
                s = '%Y-%m-%dT%H:%M:%S.%f'
                self.created_at = datetime.strptime(self.created_at, s)
                self.updated_at = datetime.strptime(self.updated_at, s)
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
        """returns a string"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """updates the public instance attribute with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing all keys/values of __dict__"""
        dontbeaDict = self.__dict__.copy()
        dontbeaDict['__class__'] = self.__class__.__name__
        dontbeaDict['created_at'] = self.created_at.isoformat()
        dontbeaDict['updated_at'] = self.updated_at.isoformat()
        return dontbeaDict
