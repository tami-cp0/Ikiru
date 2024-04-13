#!/usr/bin/python3
"""Conversation model for Ikiru web app"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from model.base_model import Base, BaseModel


class Conversation(BaseModel, Base):
    """Conversation Class"""
    user_id = Column(String(60), ForiegnKey(user.id), nullable=False)
    user = relationship("User")
    message = relationship("Messages")
