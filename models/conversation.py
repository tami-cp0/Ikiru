#!/usr/bin/python3
"""Conversation model for Ikiru web app"""
from sqlalchemy import Column, foreignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Conversations(BaseModel, Base):
    """Conversation Class"""
    __tablename__ = "conversations"
    user_id = Column(String(33), ForeignKey("users.id"), nullable=False)
    user = relationship("Users")
    message = relationship("Messages",
                           back_popluates="conversation",
                           cascade="all, delete")
