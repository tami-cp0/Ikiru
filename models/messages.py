#!/usr/bin/python3
"""Message model for Ikiru web app"""
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from model.base_model import Base, BaseModel


class Messages(BaseModel, Base):
    """Message Class"""
    # question on content field
    content = Column(Text(2048), nullable=False)
    conversation_id = Column(
            String(60), foriegnKey(conversation.id) nullable=False)
    conversations = relationship(
            "Conversation", back_populates="message", cascade="all, delete")
    user_id = Column(String(60), ForiegnKey(user.id), nullable=False)
    user = relationship("User")
