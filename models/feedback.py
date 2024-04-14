#!/usr/bin/python3
""" holds class comment"""

import models
from models.base_model2 import BaseModel2
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base


class Feedback(BaseModel2, Base):
    """Representation of a feedback"""
    __tablename__ = 'feedbacks'
    text = Column(String(255), nullable=False)

    # Foreign keys
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
