#!/usr/bin/python3


""" Convert the dictionary representation to a JSON string """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    models_dict = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                   "City": City, "Place": Place, "State": State,
                   "Review": Review}

    def all(self):
        """Returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        ser_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as f:
            for value in all_dict.values():
                key = "{}.{}".format(value.__class__.__name__, value.id)
                ser_dict[key] = value.to_dict()
            json.dump(ser_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists, otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        # Validate if file exists
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                des_json = json.load(f)
                for key, value in des_json.items():
                    # Separate name_class from id and split the separator
                    k = key.split('.')
                    # search "__class__": "BaseModel"
                    class_name = k[0]
                    # set in __objects the key, value
                    self.new(eval("{}".format(class_name))(**value))
