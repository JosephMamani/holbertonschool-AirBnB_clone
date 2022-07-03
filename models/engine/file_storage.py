#!/usr/bin/python3
"""
This file defines the FileStorage class
"""

#draft

class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key
        key_name = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({key_name: obj})
        """

    def save(self):
        """Serializes __objects to the JSON file"""
        
    def reload(self):
        """Deserializes the JSON file to __objects"""
