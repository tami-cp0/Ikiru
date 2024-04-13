#!/usr/bin/python3
""" holds class comment"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Comment(BaseModel, Base):
    """Representation of a comment """
    __tablename__ = 'comments'
    text = Column(String(255), nullable=False)
    is_reported = Column(Boolean, default=False)
    is_anonymous = Column(Boolean, default=False)

    # Foreign keys
    user_id = Column(String(33), ForeignKey('users.id'), nullable=False)
    post_id = Column(String(33), ForeignKey('posts.id'), nullable=False)

    # relationships
    reported_comments = relationship("ReportedComment", backref="comment",
                                     cascade="all, delete, delete-orphan")
