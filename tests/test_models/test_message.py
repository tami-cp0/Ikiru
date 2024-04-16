#!/usr/bin/python3
"""test message model"""
from datetime import datetime
import inspect
import pep8
import unitest
from models.base_model import BaseModel
from models.conversation import Conversation
from models.message import Message
from models.user import User


class testMessageDoc(unitest.TestCase):
    """Test the doc and style of Message class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.messagemethods = inspect.getmembers(Message, inspect.isfunction)


    def test_message_pep8_style(self):
        """test pycodestyle of message and test_message models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/message"])
        self.assertEqual(test.total_errors, 0,
                         f"pycodestyle error in {test.filename}")
    def test_module_docstring(self):
         """Test the message model docstring"""
         self.assertIsNot(Message.__doc__, None,
                          "messages.py needs docstring")
         self.assertTrue(len(Message.__doc__) >= 1,
                         "message.py needs a docstring")


    def test_message_method_docstring(self):
        """check docstring for message class methods"""
        for method in self.messagemethod:
            self.assertIsNot(method[1].__doc__, None, f"{method[0]} in
                             {inspect.getfiles(Message)} needs a docstring")
            self.assertTrue(len(method[1].__doc__) >= 1, f"{method[0]} in
            {inspect.getfiles(Message)} needs a docstring")


class testMessage(unitest.TestCase):
    """Test the attributes and methods of the message class"""
    def test_message_super_class_attr(self):
        """test the super class attributes"""
        message = Message()
        self.assertTrue(hasattr(message, "id"))
        self.assertTrue(hasattr(message, "created_at"))
        self.assertTrue(hasattr(message, "updated_at"))
        self.assertFalse(message.id == None)
        self.assertFalse(message.created_at == None)
        self.assertFalse(message.updated_at == None)


    def test_message_class_attr(self):
        """test the super class attributes"""
        message = Message()
        self.assertTrue(hasattr(message, "conversation"))
        self.assertTrue(hasattr(message, "conversation_id"))
        self.assertTrue(hasattr(message, "content"))
        self.assertTrue(hasattr(message, "user_id"))
