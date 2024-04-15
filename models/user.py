#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from models.post import Post
from models.comment import Comment
from models.conversation import Conversation
from models.message import Message
from models.feedback import Feedback
from models.reported_user import ReportedUser
import sqlalchemy
from sqlalchemy import Column, String, Date, Boolean
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
    dob = Column(Date, nullable=False)

    # things not added to data model
    name = Column(String(16), nullable=False)
    bio = Column(String(128), nullable=True)

    # relationships
    posts = relationship("Post", back_populates="user",
                         cascade="all, delete, delete-orphan")
    comments = relationship("Comment", back_populates="user",
                            cascade="all, delete, delete-orphan")
    conversations = relationship("Conversation", back_populates="user",
                                 cascade="all, delete, delete-orphan")
    messages = relationship("Message", back_populates="user",
                            cascade="all, delete, delete-orphan")
    # no deleting of child because we may still need feedback
    feedbacks = relationship("Feedback", back_populates="user")
    reported_u = relationship("ReportedUser", back_populates="reported_user")
    # reporting_u = relationship("ReportedUser", back_populates="user")
