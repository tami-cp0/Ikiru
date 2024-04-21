#!/usr/bin/python3
"""test message model"""
from datetime import  date
import inspect
import pep8
import unittest
from models import storage
from models.conversation import Conversation
from models.user import User


class testConversationDoc(unittest.TestCase):
    """Test the doc and style of Conversation class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.conversmethods = inspect.getmembers(
                Conversation, inspect.isfunction)
        # Creating a user
        cls.user = User(username="ikiru9", sex="M", email="ikiru9@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        cls.user.save()
        cls.user1 = User(username="ikiru909", sex="M", email="ikiru909@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        cls.user1.save()
        # Creating a conversation with the user id
        cls.conversation = Conversation(sender_id=self.user.id, receiver_id=user1.id)
        cls.conversation.save()
        
   
    @classmethod
    def tearDownClass(cls):
        """delete class instance use for the test"""
        # Delete created user
        cls.user.delete()
        cls.user.delete()
        # Delete created conversation
        cls.conversation.delete()
        storage.save()


    def test_conversation_pep8_style(self):
        """test pycodestyle of user and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/conversation.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the conversation model docstring"""
         self.assertIsNot(Conversation.__doc__, None,
                          "conversation.py needs docstring")
         self.assertTrue(len(Conversation.__doc__) >= 1,
                         "conversation.py needs a docstring")


    def test_conversation_method_docstring(self):
        """check docstring for conversation class methods"""
        for method in self.conversmethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)


    def test_conversation_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.conversation, "id"))
        self.assertTrue(hasattr(self.conversation, "created_at"))
        self.assertTrue(hasattr(self.conversation, "updated_at"))
        self.assertFalse(self.conversation.id == None)
        self.assertFalse(self.conversation.created_at == None)
        self.assertFalse(self.conversation.updated_at == None)


    def test_conversation_class_attr(self):
        """test the super class attributes"""
        # test the if the class instance has the class attribute
        self.assertTrue(hasattr(self.conversation, "sender_id"))
        self.assertTrue(hasattr(self.conversation, "receiver_id"))

        #Test the attribute values
        self.assertTrue(self.conversation.sender_id != None)
        self.assertTrue(self.conversation.receiver_id != None)


    def test_conversation_methods(self):
        """test conversation inherited method"""
        c_dict = self.conversation.to_dict()
        self.assertEqual(type(c_dict), dict)
        self.assertFalse("_sa_instance_state" in c_dict)
        self.assertTrue("__class__" in c_dict)
        for attr in c_dict.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in c_dict)
        self.assertEqual(self.conversation.__class__, "Conversation")
        self.assertEqul(type(self.conversation.id), str)
        self.assertEqul(type(self.conversation.created_at), str)
        self.assertEqul(type(self.conversation.updated_at), str)
        self.assertEqul(type(self.conversation.sender_id), str)
        self.assertEqul(type(self.conversation.receiver_id), str)


    def test_conversation_save_and_delete_methods(self):
        """Test conversation save and delete methods"""
        user = self.user = User(
                username ="ikiruj889unior", sex="M", email="ikiru76@ikiru.com",
                name="Ikiru junior", dob=date(2000, 4, 10), password="ikiru")
        conversation = Conversation(user_id=user.id)
        conversation.save()
        #Testt save method
        conversation_copy = storage.get(Conversation, conversation.id)
        self.assertEqual(conversation_copy, conversation)
        self.assertEqual(conversation_copy.id, conversation.id)
        self.assertEqual(conversation_copy.user_id, conversation.user_id)
        # test the delete method
        conversation_copy.delete()
        storage.save()
        self.assertEqual(storage.get(Conversation, conversation.id), None)
