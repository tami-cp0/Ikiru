#!/usr/bin/python3
"""Reportedcomments model for Ikiru web app"""
from sqlalchemy import Boolean, ForeignKey, Column, String, Text
from models.base_model2 import Base2, BaseModel2


class Reportedcomment(BaseModel2, Base2):
    """Reportecomments Class"""
    __tablename__ = "reportedcomments"
    comment_id = Column(String(33), ForeignKey("comments.id"), nullable=False)
    reporting_user = Column(
            String(33), ForeignKey("users.id"), nullable=False)
    isresolved = Column(Boolean(), default=False)
    report = Column(Text(2048), nullable=False)
