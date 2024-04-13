#!/usr/bin/python3
"""Base model for reported classes"""

from datetime import datetime
from sqlalchemy import DateTime, Column
from sqlalchemy.ext.declarative import declarative_base
import models


Base2 = declarative_base()


class BaseModel2():
    """Base model for reported classes"""
    created_at = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes a base model instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.created_at = datetime.now()

    def __str__(self):
        """String representation of a Base Model instance"""
        return f"<{self.__class__.__name__}> {self.__dict__}"

    def save(self):
        """Saves a Base Model instance"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Custom dictionary representation of a Base Model instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict

    def delete(self):
        """Deletes the current instance from the database"""
        models.storage.delete(self)
