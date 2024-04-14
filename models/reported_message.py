#!/usr/bin/python3
"""Reportedmessages model for Ikiru web app"""
import sqlalchemy
import models
from sqlalchemy import Boolean, Column, ForeignKey, String
from models.base_model2 import BaseModel2
from models.base_model import Base


class ReportedMessage(BaseModel2, Base):
    """Reportedmessage Class"""
    __tablename__ = 'reported_messages'
        
    is_resolved = Column(Boolean, default=False)
    report = Column(String(2048), nullable=False)

    # Foreign keys
    message_id = Column(String(36), ForeignKey("messages.id"), nullable=False)
    reporting_user = Column(
            String(36), ForeignKey("users.id"), nullable=False)
