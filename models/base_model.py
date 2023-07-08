#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        if type(value) == str:
                            format_t = "%Y-%m-%dT%H:%M:%S.%f"
                            value = datetime.strptime(value, format_t)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        The method formats the string to include the class name, object ID,
        and the object's dictionary representation.

        Returns:
            A string representation of the object.
    """
        clsName = self.__class__.__name__
        id = self.id
        return "[{}] ({}) {}".format(clsName, id, self.__dict__)

    def save(self):
        """
        Saves the object and updates the updated_at attribute.

        The method updates the updated_at attribute with the current datetime,
        adds the object to the storage, and saves the storage.

        Returns:
            None
    """
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Converts the object into a dictionary representation.

        The method creates a new dictionary and copies the object's attributes
        into the new dictionary.
        The __class__ attribute is added to represent
        the class name of the object

        Returns:
            A dictionary representing the object.
    """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
