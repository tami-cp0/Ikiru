#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    username = Column(String(32), nullable=False)
    email = Column(String(32), nullable=False)
    sex = Column(String(16), nullable=False)
    password = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    # enter base model to change
    dob = Column(DateTime, nullable=False)
    # things not added to data model
    name = Column(String(16), nullable=False)
    bio = Column(String(128), nullable=True)

    # relationships
    posts = relationship("Post", backref="user",
                         cascade="all, delete, delete-orphan")
    comments = relationship("Comment", backref="user",
                            cascade="all, delete, delete-orphan")
    conversations = relationship("Conversation", backref="user",
                                 cascade="all, delete, delete-orphan")
    feedbacks = relationship("Feedback", backref="user")
    reported_user = relationship("ReportedUser", backref="user",
                                 cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    # password hash will be thought about later.
