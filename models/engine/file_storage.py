#!/usr/bin/python3


"""This module defines a class to manage file storage for hbnb clone"""


from importlib import import_module
import pathlib
import json


from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        if not cls:
            return FileStorage.__objects
        return {
            identifier: obj
            for identifier, obj in FileStorage.__objects.items()
            if cls is obj.__class__
        }

    def close(self):
        """Deserialised JSON file to objects"""

        self.reload()

    def delete(self, obj=None):
        """Deletes obj from storage"""

        if obj:
            identifier = f"{obj.to_dict()['__class__']}.{obj.id}"
            FileStorage.__objects.pop(identifier)
            self.save()

    def new(self, obj):
        """Adds new object to storage dictionary"""

        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""

        if not self.all():
            return

        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }

        path = pathlib.Path(FileStorage.__file_path)

        if not path.is_file():
            return

        if not path.stat().st_size:
            raise ValueError("file is empty")

        temp = {}

        with open(FileStorage.__file_path, "r") as file:
            if not file:
                raise ValueError("file is empty")

            temp = json.load(file)

            for key, val in temp.items():
                self.all()[key] = classes[val["__class__"]](**val)
