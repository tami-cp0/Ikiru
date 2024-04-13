#!/usr/bin/python3
""" holds class comment"""

import models
from models.base_model2 import BaseModel2, Base2
import sqlalchemy
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Feedback(BaseModel2, Base2):
    """Representation of a feedback"""
    __tablename__ = 'feedbacks'
    text = Column(String(255), nullable=False)

    # Foreign keys
    user_id = Column(String(33), ForeignKey('users.id'), nullable=False)
