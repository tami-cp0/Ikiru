#!/usr/bin/python3
"""Conversation model for Ikiru web app"""
from sqlalchemy import Column, foreignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Conversation(BaseModel, Base):
    """Conversation Class"""
    user_id = Column(String(33), ForeignKey("user.id"), nullable=False)
    user = relationship("User")
    message = relationship("Messages", back_popluates="conversation", cascade="all, delete")
