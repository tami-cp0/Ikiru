#!/usr/bin/python3
"""Base model for all main ikiru models"""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import DateTime, Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
import models


class BaseModel2():
    """Base model from which future main classes will be derived"""
    id = Column(String(36), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes a base model instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
            if kwargs.get("created_at", None) is None:
                self.created_at = datetime.now()

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """String representation of a Base Model instance"""
        return f"<{self.__class__.__name__}> <{self.id}> {self.__dict__}"

    def save(self):
        """Updates and saves a Base Model instance"""
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
