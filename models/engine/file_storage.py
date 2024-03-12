#!/usr/bin/python3
"""
Defines the FileStorage class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj_id, obj in obj_dict.items():
                    cls_name = obj["__class__"]
                    if cls_name == "User":
                        del obj["__class__"]
                        self.new(User(**obj))
                    elif cls_name == "State":
                        del obj["__class__"]
                        self.new(State(**obj))
                    elif cls_name == "City":
                        del obj["__class__"]
                        self.new(City(**obj))
                    elif cls_name == "Amenity":
                        del obj["__class__"]
                        self.new(Amenity(**obj))
                    elif cls_name == "Place":
                        del obj["__class__"]
                        self.new(Place(**obj))
                    elif cls_name == "Review":
                        del obj["__class__"]
                        self.new(Review(**obj))
        except FileNotFoundError:
            return
