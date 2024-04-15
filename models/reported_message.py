#!/usr/bin/python3
"""Reportedmessages model for Ikiru web app"""
import sqlalchemy
import models
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model2 import BaseModel2
from models.base_model import Base


class ReportedMessage(BaseModel2, Base):
    """Reportedmessage Class"""
    __tablename__ = 'reported_messages'

    is_resolved = Column(Boolean, default=False)
    content = Column(String(255), nullable=False)

    # Foreign keys
    message_id = Column(String(36), ForeignKey("messages.id"), nullable=False)
    reporting_user = Column(
        String(36), ForeignKey("users.id"), nullable=False)

    # Relationships
    message = relationship("Message", back_populates="reports")
    user = relationship("User", back_populates="reported_messages")
