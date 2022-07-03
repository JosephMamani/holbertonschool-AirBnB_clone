#!/usr/bin/python3
"""
Defines BaseModel class
"""
#import uuid
from datetime import datetime

class BaseModel():
    """
    Defines all common  attributes/methods for other classes
    """

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,self.id,self.__dict__))

    def save(self):
        """
        Updates the public instance attribute
        """
        self.updated_at = datetime.now()

        """
        from models.__init__ import storage
        storage.save()
        """
        #para revisar esta parte

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary.update({"created_at": self.created_at.isoformat()})
        dictionary.update({"updated_at": self.updated_at.isoformat()})
        return dictionary
