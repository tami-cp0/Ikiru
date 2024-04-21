#!/usr/bin/python3
"""Conversation model for Ikiru web app"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Conversation(BaseModel, Base):
    """Conversation Class"""
    __tablename__ = "conversations"
    sender_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    receiver_id = Column(String(36), ForeignKey("users.id"), nullable=False)

    # Relationships
    sender = relationship(
        "User",
        foreign_keys=[sender_id],
        back_populates="sent_conversation"
    )
    receiver = relationship(
        "User",
        foreign_keys=[receiver_id],
        back_populates="received_conversation"
    )
    messages = relationship("Message",
                           back_populates="conversation",
                           cascade="all, delete, delete-orphan")
