#!/usr/bin/python3
"""Base model for all ikiru models"""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel():
    """Base model from which future classes will be derived"""
    id = Column(String(33), primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
