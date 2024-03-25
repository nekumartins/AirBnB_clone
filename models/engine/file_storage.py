#!usr/bin/python3
import json
from models.base_model import BaseModel, User


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
        except FileNotFoundError:
            pass
