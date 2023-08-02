#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of class."""
        if cls is None:
            return FileStorage.__objects
        else:
            emptyList = {}
            for k, v in FileStorage.__objects.items():
                # print(f"{FileStorage.__objects[k].__class__} ---- {cls}")
                if FileStorage.__objects[k].__class__ == cls:
                    emptyList[k] = str(v)
            return (emptyList)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """This function delete obj from __objects if it is inside - if obj
        is equal to None, the method should not do anything"""
        # Rename
        objlist = FileStorage.__objects
        # Find class name from __class__
        objClass = str(obj.__class__.__name__)
        if obj is not None:
            objKey = objClass + "." + str(obj.id)
            if objKey in objlist:
                objlist.pop(objKey)