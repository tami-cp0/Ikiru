#!/usr/bin/python3
"""test message model"""
from datetime import date
import inspect
import pep8
import unittest
from models import storage
from models.base_model import BaseModel
from models.conversation import Conversation
from models.message import Message
from models.user import User


class testMessageDoc(unittest.TestCase):
    """Test the doc and style of Message class"""
    def setUp(self):
        """set up class instance for test"""
        # Creating a user
        self.user = User(username="ikiru", sex="M", email="ikiru@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        # Creating a conversation with the user id
        self.conversation = Conversation(user_id=self.user.id)
        # Create a message with the conversation id and user id
        self.message = Message(content="What a lovely day with you Huclark", user_id=self.user.id, conversation_id = self.conversation.id)


    def tearDown(self):
        """delete class instance use for the test"""
        # Delete created user
        del self.user
        # Delete created conversation
        del self.conversation
        # Delete created message
        del self.message
   

    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.messagemethods = inspect.getmembers(Message, inspect.isfunction)


    def test_message_pep8_style(self):
        """test pycodestyle of message and test_message models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/message.py"])
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


    def test_message_super_class_attr(self):
        """test the super class attributes"""   
        self.assertTrue(hasattr(self.message, "id"))
        self.assertTrue(hasattr(self.message, "created_at"))
        self.assertTrue(hasattr(self, "updated_at"))
        self.assertFalse(self.message.id == None)
        self.assertFalse(self.message.created_at == None)
        self.assertFalse(self.message.updated_at == None)


    def test_message_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.message, "conversation_id"))
        self.assertTrue(hasattr(self.message, "content"))
        self.assertTrue(hasattr(self.message, "user_id"))
        self.assertFalse(self.message.conversation_id == None)
        self.assertFalse(self.message.content == None)
        self.assertFalse(self.message.updated_at == None)
        
        
    def test_message_methods(self):
        """test message inherited method"""
        m_dict = self.message.to_dict()
        self.assertEqual(type(m_dict), dict)
        self.assertFalse("_sa_instance_state" in m_dict)
        self.assertTrue("__class__" in m_dict)
        # Test the dict attribute
        for attr in m_dict.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in m_dict)

        # Test the attribute value types
        self.assertEqual(self.message.__class__, "Conversation")
        self.assertEqul(type(self.message.id), str)
        self.assertEqul(type(self.message.created_at), str)
        self.assertEqul(type(self.message.updated_at), str)
        self.assertEqul(type(self.message.user_id), str)


    def message_save_and_delete_methods(self):
        """Test message save and delete methods"""
        user = self.user = User(
                username ="ikirujunior", sex="M", email="ikiru@ikiru.com",
                name="Ikiru junior", dob=date(2000, 4, 10), password="ikiru")
        user.save()
        conversation = Conversation(user_id=user.id)
        conversation.save()
        message = Message(content="Good", user_id=self.user.id, conversation_id = self.conversation.id)

        message.save()
        #Testt save method
        message_copy = storage.get(Message, message.id)
        self.assertEqual(message_copy, message)
        self.assertEqual(message_copy.id, message.id)
        self.assertEqual(message_copy.user_id, message.user_id)
        # test the delete method
        message_copy.delete()
        storage.save()
        self.assertEqual(storage.get(Message, message.id), None)
