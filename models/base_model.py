#!/usr/bin/python3
"""doc"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """doc"""

    def __init__(self, *args, **kwargs):
        """doc"""
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
        """doc"""
        clsName = self.__class__.__name__
        id = self.id
        return "[{}] ({}) {}".format(clsName, id, self.__dict__)

    def save(self):
        """doc"""
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """doc"""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
