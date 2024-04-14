#!/usr/bin/python3
"""Reportedcomments model for Ikiru web app"""
import sqlalchemy
import models
from sqlalchemy import Boolean, ForeignKey, Column, String
from models.base_model2 import BaseModel2
from models.base_model import Base


class ReportedComment(BaseModel2, Base):
    """Reportecomments Class"""
    __tablename__ = 'reported_comments'

    is_resolved = Column(Boolean, default=False)
    report = Column(String(2048), nullable=False)

    # Foreign keys
    comment_id = Column(String(36), ForeignKey("comments.id"), nullable=False)
    reporting_user = Column(
            String(36), ForeignKey("users.id"), nullable=False)
