#!/usr/bin/python3
"""Message model for Ikiru web app"""
from sqlalchemy import Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Message(BaseModel, Base):
    """Message Class"""
    __tablename__ = "messages"
    content = Column(String(255), nullable=False)
    is_reported = Column(Boolean, default=False)

    # Foreign keys
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    conversation_id = Column(
        String(36), ForeignKey("conversations.id"), nullable=False
    )

    # Relationships
    conversation = relationship("Conversation", back_populates="messages")
    user = relationship("User", back_populates="messages")
    reports = relationship(
        "ReportedMessage", back_populates="message", cascade="all, delete, delete-orphan")
