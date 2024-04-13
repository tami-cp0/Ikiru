#!/usr/bin/python3
"""Reportedcomments model for Ikiru web app"""
from sqlalchemy import Boolean, ForeignKey, Column, String, Text
from models.base_model2 import Base2, BaseModel2


class Reportedcomments(BaseModel2, Base2):
    """Reportecomments Class"""
    comment_id = Column(String(33), ForeignKey("comment.id"), nullable=False)
    reporting_user = Column(
            String(33), ForeignKey("user.id"), nullable=False)
    isresolved = Column(Boolean(), default=False)
    report = Column(Text(2048), nullable=False)
