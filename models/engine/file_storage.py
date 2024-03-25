#!usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            objects = {
                k: v.to_dict() for k, v in FileStorage.__objects.items()
                }
            json.dump(objects, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for obj in objs.values():
                cls = obj['__class__']
                if cls == 'User':
                    self.new(User(**obj))
                elif cls == 'BaseModel':
                    self.new(BaseModel(**obj))
                elif cls == 'State':
                    self.new(State(**obj))
                elif cls == 'City':
                    self.new(City(**obj))
                elif cls == 'Amenity':
                    self.new(Amenity(**obj))
                elif cls == 'Place':
                    self.new(Place(**obj))
                elif cls == 'Review':
                    self.new(Review(**obj))
        except FileNotFoundError:
            return
