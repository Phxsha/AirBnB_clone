#!/usr/bin/python3
"""Module containing the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances

    Attributes:
    __file_path (str): Name of file
    __objects (dict): Dictionary of the objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file."""
        with open(FileStorage.__file_path, "w") as file:
            obj_dict = {key:obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split(".")
                    obj = eval(cls_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

