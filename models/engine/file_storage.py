#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}
    
    def all(self):

        return self.__objects

    def new(self, obj):

        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):

        dic_objects = {}
        for key, value in self.__objects.items():
            dic_objects[key] = value.to_dict()
        with open(self.__file_path, 'w+') as f:
            json.dump(dic_objects, f)

    def reload(self):
        
        try:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value['__class__'] + '(**value)')
        except FileNotFoundError:
            return
