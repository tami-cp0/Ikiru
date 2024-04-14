#!/usr/bin/python3
"""This module defines a class to manage storage for Ikiru"""

from os import getenv
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
           "Conversation": Conversation, "Message": Message, "ReportedUser": ReportedUser,
           "ReportedComment": ReportedComment, "ReportedMessage": ReportedMessage}

    def __init__(self):
        """Initializes a DBStorage instance"""
        username = "ikiru_user"
        password = "password"
        hostname = "localhost"
        database = "ikiru_dev_db"
        running_environment = "dev"
        self.__engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@{hostname}/{database}",
            pool_pre_ping=True
        )

        if running_environment == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects. If a table is specified,
        It will return all objects of the specified table

        Args:
            cls (Class, optional): The table to query. Defaults to None.

        Returns:
            dict: A dictionary of all the objects
        """
        all_objects = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                all_objects[key] = obj
        else:
            for table in self.tables.values():
                objs = self.__session.query(table).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    all_objects[key] = obj

        return all_objects

    def new(self, obj):
        """Adds an object to the current database session

        Args:
            obj (instance of a class): An instance of a class
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session

        Args:
            obj (instance, optional): Object to delete. Defaults to None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and establishes a session from
        the engine
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )

    def close(self):
        """Closes the current database session
        """
        self.__session.remove()
