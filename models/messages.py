#!/usr/bin/python3
"""Message model for Ikiru web app"""
from sqlalchemy import Column, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Message(BaseModel, Base):
    """Message Class"""
    __table__name = "messages"
    content = Column(Text(2048), nullable=False)
    conversation_id = Column(
            String(33), ForeignKey("conversations.id") nullable=False)
    conversation = relationship("Conversation")
    user_id = Column(String(33), ForeignKey("users.id"), nullable=False)
    user = relationship("User")
