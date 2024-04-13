#!/usr/bin/python3
"""Reportedmessages model for Ikiru web app"""
from sqlalchemy import Column, String, Text, Boolean
from models.base_model2 import Base2, BaseModel2


class Reportedmessages(BaseModel2, Base2):
    """Reportedmessage Class"""
    message_id = Column(String(60), ForiegnKey(message.id), nullable=False)
    reporting_user = Column(
            String(60), ForiegnKey(user.id), nullable=False)
    isresolved = Column(Boolean(), default=False)
    report = Column(Text(2048), nullable=False)
