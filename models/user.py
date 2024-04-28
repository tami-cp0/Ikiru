#!/usr/bin/python3
""" holds class User"""
from sqlalchemy import Column, String, Date
from sqlalchemy import Boolean, Integer, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from flask_login import UserMixin


# follower_following_association = Table(
#     'follower_following_associations',
#     Base.metadata,
#     Column('follower_id', String(36), ForeignKey('users.id')),
#     Column('following_id', String(36), ForeignKey('users.id')),
#  UniqueConstraint('follower_id', 'following_id', name='unique_relationship')
# )

class User(BaseModel, Base, UserMixin):
    """Representation of a user """
    __tablename__ = 'users'
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(32), unique=True, nullable=False)
    sex = Column(String(16), nullable=True)
    password = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    is_reported = Column(Boolean, default=False)
    # Relationship to represent users following other users
    # and vice versa
    # following = relationship("User",
    #                          secondary=follower_following_association,
    #                          primaryjoin=id==follower_following_association.c.follower_id,
    #                          secondaryjoin=id==follower_following_association.c.following_id,
    #                          backref="followers")

    # enter base model to change
    dob = Column(Date, nullable=True)

    # things not added to data model
    name = Column(String(16), nullable=False)
    bio = Column(String(128), nullable=True)

    # relationships
    posts = relationship("Post", back_populates="user",
                         cascade="all, delete, delete-orphan")
    comments = relationship("Comment", back_populates="user",
                            cascade="all, delete, delete-orphan")
    sent_conversations = relationship(
        "Conversation",
        back_populates="sender",
        foreign_keys="[Conversation.sender_id]",
        cascade="all, delete, delete-orphan",
    )
    received_conversations = relationship(
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

    # def follow(self, user):
    #     if user not in self.following:
    #         self.followers.append(user)
    #         user.followers.append(self)

    # def unfollow(self, user):
    #     if user not in self.followers:
    #         self.following.remove(user)
    #         user.following.remove(self)
    
    def get_id(self):
        return str(self.id)
