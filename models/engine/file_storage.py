#!/usr/bin/python3
"""class FileStorage"""
from json import dumps, loads
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Serialize instances to a Json file
    And deserialize Json file to instances
Attrs:
    __file_path(str): Path of the JSOn file
    __objects(dict): Storage of all objects by <class name>.id
    """
    __file_path = "models/engine/file.json"
    __objects = {}

    def all(self):
        """Return the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in '__objects' the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, mode="w") as f:
            json_dict = {}
            for key, obj in FileStorage.__objects.items():
                json_dict[key] = obj.to_dict()
            f.write(dumps(json_dict))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                json_dict = loads(f.read())
                for key, obj_dict in json_dict.items():
                    obj_class = str(obj_dict['__class__']) + "(**obj_dict)"
                    FileStorage.__objects[key] = eval(obj_class)
        except Exception:
            pass
