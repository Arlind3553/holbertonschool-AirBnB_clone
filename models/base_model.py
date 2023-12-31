#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        '''
        Init function for BaseModel instances
        '''
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        '''
        Function to update the 'updated_at' attribute
        of the instance when updated
        '''
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
        return self.updated_at

    def __str__(self):
        '''
        String representation of the instance
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        '''
        Dictionary representation of the instance
        '''
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
