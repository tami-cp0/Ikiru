#!/usr/bin/python3
"""Reportedusers model for Ikiru web app"""
from sqlalchemy import Boolean, ForeignKey, Column, String
from sqlalchemy.orm import relationship
from models.base_model2 import BaseModel2
from models.base_model import Base


class ReportedUser(BaseModel2, Base):
    """Reportedcoment Class"""
    __tablename__ = 'reported_users'

    is_resolved = Column(Boolean, default=False)
    content = Column(String(255), nullable=False)

    # Foreign Keys
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)

    # Relationships
    reported_user = relationship("User", back_populates="report")
