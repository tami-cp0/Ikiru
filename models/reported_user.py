#!/usr/bin/python3
"""Reportedusers model for Ikiru web app"""
import sqlalchemy
import models
from sqlalchemy import Boolean, ForeignKey, Column, String
from models.base_model2 import BaseModel2
from models.base_model import Base


class ReportedUser(BaseModel2, Base):
    """Reportedcoment Class"""
    __tablename__ = 'reported_users'

    is_resolved = Column(Boolean, default=False)
    report = Column(String(2048), nullable=False)

    # Foreign Keys
    reported_user = Column(String(36), ForeignKey('users.id'), nullable=False)
    
    # you cant use two foreign keys referring to the same column
    # so we'll get the id of the user reporting, later during backend parsing.
    # reporting_user = Column(
            # String(33), ForeignKey('users.id'), nullable=False)
