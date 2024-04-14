#!/usr/bin/python3
""" holds class comment"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.reported_comment import ReportedComment


class Comment(BaseModel, Base):
    """Representation of a comment """
    __tablename__ = 'comments'
    text = Column(String(255), nullable=False)
    is_reported = Column(Boolean, default=False)
    is_anonymous = Column(Boolean, default=False)

    # Foreign keys
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    post_id = Column(String(36), ForeignKey('posts.id'), nullable=False)

    # relationships
    user = relationship("User", back_populates="comments")
    reported_comments = relationship("ReportedComment", back_populates="comment")
