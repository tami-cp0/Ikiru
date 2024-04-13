#!/usr/bin/python3
""" holds class comment"""

import models
from models.base_model2 import BaseModel2, Base2
import sqlalchemy
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class ReportedPost(BaseModel2, Base2):
    """Representation of a reported posts """
    __tablename__ = 'reported_posts'
    text = Column(String(255), nullable=False)

    # Foreign keys
    user_id = Column(String(33), ForeignKey('users.id'), nullable=False)
    post_id = Column(String(33), ForeignKey('posts.id'), nullable=False)
