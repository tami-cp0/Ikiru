#!/usr/bin/python3
"""Base model for all ikiru models"""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base
import models


Base = declarative_base()


class BaseModel():
    """Base model from which future classes will be derived"""
    id = Column(String(33), primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

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
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of a Base Model instance"""
        return f"<{self.__class__.__name__}> <{self.id}> {self.__dict__}"

    def save(self):
        """Updates and saves a Base Model instance"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Custom dictionary representation of a Base Model instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """Deletes the current instance from the database"""
        models.storage.delete(self)
