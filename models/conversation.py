#!/usr/bin/python3
"""Conversation model for Ikiru web app"""
import models
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Conversation(BaseModel, Base):
    """Conversation Class"""
    __tablename__ = "conversations"
    user_id = Column(String(33), ForeignKey("users.id"), nullable=False)
    user = relationship("Users")
    message = relationship("Message",
                           back_popluates="conversation",
                           cascade="all, delete")
    __tablename__ = 'conversations'
    # Foreign key
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="conversations")
    messages = relationship("Message",
                           back_populates="conversations",
                           cascade="all, delete, delete-orphan")
