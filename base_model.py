#!/usr/bin/python3
"""Base model for all ikiru models"""
from datetime import datetime
from sqlalchemy import Srting, DateTime, Column
from uuid import uuid4


class BaseModel():
    """Base model  class"""
    id = 