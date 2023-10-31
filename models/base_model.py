#!/usr/bin/python3


import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.dict}"

    def to_dict(self):
        data = self.dict__copy()
        data['__class__'] = self.__class__.__name__
        data['__created_at__'] = data['__created_at__'].isoformat()
        data['__updated_at__'] = data['__updated_at__'].isoformat()
        return data
