#!/usr/bin/python3
"""Reportedmessages model for Ikiru web app"""
from sqlalchemy import Boolean, Column, ForeignKey, String, Text
from models.base_model2 import Base2, BaseModel2


class Reportedmessage(BaseModel2, Base2):
    """Reportedmessage Class"""
    __tablename__ = "reportedmessages"
    message_id = Column(String(33), ForeignKey("messages.id"), nullable=False)
    reporting_user = Column(
            String(33), ForeignKey("users.id"), nullable=False)
    isresolved = Column(Boolean(), default=False)
    report = Column(Text(2048), nullable=False)
