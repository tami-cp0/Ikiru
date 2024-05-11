#!/usr/bin/python3
"""This module defines a class to manage storage for Ikiru"""

from os import getenv
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.post import Post
from models.comment import Comment
from models.feedback import Feedback
from models.reported_post import ReportedPost
from models.conversation import Conversation
from models.message import Message
from models.reported_user import ReportedUser
from models.reported_message import ReportedMessage
from models.reported_comment import ReportedComment


class DBStorage():
    """This class manages storage of Ikiru using MySQL"""
    __engine = None
    __session = None
    tables = {"User": User, "Post": Post, "Comment": Comment,
              "ReportedPost": ReportedPost, "feedback": Feedback,
              "Conversation": Conversation, "Message": Message,
              "ReportedUser": ReportedUser, "ReportedComment": ReportedComment,
              "ReportedMessage": ReportedMessage}

    @classmethod
    def init(cls):
        """Initialize the database engine and session"""
        username = "ikiru_user"
        password = "password"
        hostname = "localhost"
        database = "ikiru_db"

        if not cls.__engine or not cls.__session:
            cls.__engine = create_engine(
                f"mysql+mysqldb://{username}:{password}@{hostname}/{database}",
                pool_pre_ping=True
            )
            Base.metadata.create_all(cls.__engine)
            cls.__session = scoped_session(
                sessionmaker(bind=cls.__engine, expire_on_commit=False)
            )

    @classmethod
    def all(cls, class_name=None):
        """Returns a dictionary of all objects. If a table is specified,
        It will return all objects of the specified table

        Args:
            cls (Class, optional): The table to query. Defaults to None.

        Returns:
            dict: A dictionary of all the objects
        """

        all_objects = {}
        if class_name:
            objs = cls.__session.query(class_name).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                all_objects[key] = obj
        else:
            for table in cls.tables.values():
                objs = cls.__session.query(table).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    all_objects[key] = obj

        return all_objects
    
    @classmethod
    def open_session(cls):
        """Open a new session"""
        if not cls.__session:
            cls.init()

    @classmethod
    def close(cls):
        """Close the current session"""
        if cls.__session:
            cls.__session.remove()

    @classmethod
    def new(cls, obj):
        """Adds an object to the current database session

        Args:
            obj (instance of a class): An instance of a class
        """
        cls.__session.add(obj)

    @classmethod
    def save(cls):
        """Commits all changes to the current database session
        """
        cls.__session.commit()

    @classmethod
    def delete(cls, obj=None):
        """Deletes an object from the current database session

        Args:
            obj (instance, optional): Object to delete. Defaults to None.
        """
        if obj is not None:
            cls.__session.delete(obj)

    @classmethod
    def get(cls, class_name, id=None, username=None, email=None):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if class_name not in cls.tables.values():
            return None

        all_cls = models.storage.all(class_name)
        for value in all_cls.values():
            if id:
                if (value.id == id):
                    return value
            if username:
                if (value.username == username):
                    return value
            if email:
                if (value.email == email):
                    return value

        return None

    @classmethod
    def count(cls, class_name=None):
        """
        count the number of objects in storage
        """
        all_class = cls.tables.values()

        if not class_name:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(class_name).values())

        return count
