#!/usr/bin/python3
""" holds class User"""

from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(32), unique=True, nullable=False)
    sex = Column(String(16), nullable=False)
    password = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    is_reported = Column(Boolean, default=False)

    # enter base model to change
    dob = Column(Date, nullable=False)

    # things not added to data model
    name = Column(String(16), nullable=False)
    bio = Column(String(128), nullable=True)

    # relationships
    posts = relationship("Post", back_populates="user",
                         cascade="all, delete, delete-orphan")
    comments = relationship("Comment", back_populates="user",
                            cascade="all, delete, delete-orphan")
    sent_conversation = relationship(
        "Conversation",
        back_populates="sender",
        foreign_keys="[Conversation.sender_id]",
        cascade="all, delete, delete-orphan",
    )
    received_conversation = relationship(
        "Conversation",
        back_populates="receiver",
        foreign_keys="[Conversation.receiver_id]",
        cascade="all, delete, delete-orphan",
    )
    messages = relationship("Message", back_populates="user",
                            cascade="all, delete, delete-orphan")
    # no deleting of child because we may still need feedback
    feedbacks = relationship("Feedback", back_populates="user")
    report = relationship(
        "ReportedUser", back_populates="reported_user",
        cascade="all, delete, delete-orphan")
    reported_comments = relationship(
        "ReportedComment", back_populates="user",
        cascade="all, delete, delete-orphan")
    reported_posts = relationship(
        "ReportedPost", back_populates="user",
        cascade="all, delete, delete-orphan")
    reported_messages = relationship(
        "ReportedMessage", back_populates="user",
        cascade="all, delete, delete-orphan"
    )
    # reporting_u = relationship("ReportedUser", back_populates="user")
