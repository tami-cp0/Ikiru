#!/usr/bin/python3
"""Conversation model for Ikiru web app"""
import models
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Conversation(BaseModel, Base):
    """Conversation Class"""
    __tablename__ = "conversations"
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="conversations")
    messages = relationship("Message",
                           back_populates="conversation",
                           cascade="all, delete, delete-orphan")
