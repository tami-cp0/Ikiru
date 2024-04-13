#!/usr/bin/python3
""" holds class comment"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    """Representation of a comment """
    __tablename__ = 'comments'
    text = Column(String(255), nullable=False)
    
    # Foreign keys
    user_id = Column(String(33), ForeignKey('users.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes comment"""
        super().__init__(*args, **kwargs)
