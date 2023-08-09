#!/usr/bin/python3
"""class BaseModel"""
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Define all common attrbutes/methods for other classes
Args:
    id(str): unique id created using uuid.uuid4()
    created_at(datetime): datetime of the creation of an instance
    updated_at(datetime): datetime of the update of an instance
    """
    def __init__(self, *args, **kwargs):
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    date_format = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update 'updated_at' with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return a dict of keys/valus of the instance"""
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
