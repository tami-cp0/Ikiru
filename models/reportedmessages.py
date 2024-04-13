#!/usr/bin/python3
"""Conversation model for Ikiru web app"""
from sqlalchemy import Column, String, Text, Boolean
from sqlalchemy.orm import relationship
from model.base_model import Base, BaseModel


class Conversation(BaseModel, Base):
    """Conversation Class"""
    comment_id = Column(String(60), ForiegnKey(comment.id), nullable=False)
    reporting_user = Column(
            String(60), ForiegnKey(user.id), nullable=False)
    isresolved = Column(Boolean(), default=False)
    report = Column(Text(2048), nullable=False)
