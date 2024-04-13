#!/usr/bin/python3
"""Message model for Ikiru web app"""
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Messages(BaseModel, Base):
    """Message Class"""
    content = Column(Text(2048), nullable=False)
    conversation_id = Column(
            String(60), foriegnKey(conversation.id) nullable=False)
    conversations = relationship("Conversation")
    user_id = Column(String(60), ForiegnKey(user.id), nullable=False)
    user = relationship("User")
