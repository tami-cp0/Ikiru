#!/usr/bin/python3
"""Reportedusers model for Ikiru web app"""
from sqlalchemy import Boolean, foreignKey, Column, String, Text, Boolean
from models.base_model2 import Base2, BaseModel2


class Reportedusers(BaseModel2, Base2):
    """Reportedcoment Class"""
    reported_user = Column(String(33), ForeignKey('user.id'), nullable=False)
    reporting_user = Column(
            String(33), ForeignKey('user.id'), nullable=False)
    isresolved = Column(Boolean(), default=False)
    report = Column(Text(2048), nullable=False)
