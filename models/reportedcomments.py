#!/usr/bin/python3
"""Reportedcomments model for Ikiru web app"""
from sqlalchemy import Column, String, Text, Boolean
from models.base_model2 import Base2, BaseModel2


class Reportedcomments(BaseModel2, Base2):
    """Reportecomments Class"""
    message_id = Column(String(60), ForiegnKey(message.id), nullable=False)
    reporting_user = Column(
            String(60), ForiegnKey(user.id), nullable=False)
    isresolved = Column(Boolean(), default=False)
    report = Column(Text(2048), nullable=False)
