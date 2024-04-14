#!/usr/bin/python3
""" holds class comment"""

import models
from models.base_model2 import BaseModel2
import sqlalchemy
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base



class ReportedPost(BaseModel2, Base):
    """Representation of a reported posts """
    __tablename__ = 'reported_posts'

    is_resolved = Column(Boolean, default=False)
    text = Column(String(255), nullable=False)

    # Foreign keys
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    post_id = Column(String(36), ForeignKey('posts.id'), nullable=False)
