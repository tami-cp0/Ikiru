#!/usr/bin/python3
""" holds class Post"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    """Representation of a post"""
    __tablename__ = 'posts'
    text = Column(String(255), nullable=False)
    is_reported = Column(Boolean, default=False)
    is_anonymous = Column(Boolean, default=False)

    # Foreign keys
    user_id = Column(String(33), ForeignKey('users.id'), nullable=False)

    # relationships
    comments = relationship("Comment", backref="post")
    reported_posts = relationship("ReportedPost", backref="post")


    def __init__(self, *args, **kwargs):
        """initializes post"""
        super().__init__(*args, **kwargs)