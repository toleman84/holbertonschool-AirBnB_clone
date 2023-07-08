#!/usr/bi/python3
"""Defines the FileStorage class."""
import json
import re

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """that serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects (__objects).

        The method retrieves and returns the dictionary of objects (__objects)
        stored in the class.

        Returns:
            The dictionary of objects (__objects).
        """
        return self.__class__.__objects

    def new(self, obj):
        """Adds the object into an objects list

        Args:
            obj (object): Object to add
        """
        self.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        """
        Saves the objects stored in the __objects dictionary to a JSON file.

        The method iterates through the __objects dictionary
        and converts each object to a dictionary
        using its to_dict() method, then the dictionaries of the objects are
        stored in a general dictionary, my_dict.

        Finally, the my_dict dictionary is saved to a JSON file specified
        by the __file_path.

        Returns:
            None
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        Reloads the objects from a JSON file and stores them in the __objects
        dictionary.

        The method attempts to open the JSON file specified by the __file_path
        in read mode.
        It iterates over the items loaded from the JSON file and converts them
        back into objects using the class information (__class__)
        and attributes from the loaded dictionary.
        The resulting objects are stored in the __objects dictionary.

        If the file specified by the __file_path does not exist
        the method handles the FileNotFoundError.

        Returns:
            None
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes the specified object from the __objects dictionary.

        If an object is provided as an argument,
        the method retrieves the key for the object in the format
        "{class_name}.{object_id}" and deletes the corresponding
        entry from the __objects dictionary.

        Args:
            obj: The object to be deleted from the __objects dictionary.

        Returns:
            None
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """
        Closes the current storage session by reloading
        the objects from the JSON file.

        The method calls the reload() method to reload
        the objects from the JSON file and update the __objects dictionary.

        Returns:
            None
        """
        self.reload()

    def get(self, objId):
        """
        Retrieves an object from the __objects dictionary based on the
        provided objId.

        The method iterates over the keys in the __objects dictionary
        and extracts the object ID from each key.
        If the extracted object ID matches the provided objId,
        the corresponding object is returned.

        Args:
            objId: The ID of the object to retrieve.

        Returns:
            The object corresponding to provided objId if found,
            None otherwise.
        """
        for key in self.all():
            result = re.sub(r'^.*?\.', '', key)
            if objId == result:
                return self.__objects[key]
        return None
