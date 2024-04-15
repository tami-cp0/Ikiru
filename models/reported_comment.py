#!/usr/bin/python3
"""Reportedcomments model for Ikiru web app"""
from sqlalchemy.orm import relationship
import models
from sqlalchemy import Boolean, ForeignKey, Column, String
from models.base_model2 import BaseModel2
from models.base_model import Base


class ReportedComment(BaseModel2, Base):
    """Reportecomments Class"""
    __tablename__ = 'reported_comments'

    is_resolved = Column(Boolean, default=False)
    content = Column(String(255), nullable=False)

    # Foreign keys
    comment_id = Column(String(36), ForeignKey("comments.id"), nullable=False)
    reporting_user = Column(
        String(36), ForeignKey("users.id"), nullable=False)

    # Relationship
    comment = relationship("Comment", back_populates="reported_comments")
    user = relationship("User", back_populates="reported_comments")
