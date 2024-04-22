#!/usr/bin/python3
"""test message model"""
from datetime import date, datetime
import inspect
import pep8
import unittest
from models import storage
from models.conversation import Conversation
from models.message import Message
from models.reported_message import ReportedMessage
from models.user import User


class testMessageDoc(unittest.TestCase):
    """Test the doc and style of reported_message class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.rmessagemethods = inspect.getmembers(ReportedMessage, inspect.isfunction)
        cls.user = User(username="ikiru4", sex="M", email="ikiru4@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        cls.user.save()
        cls.user1 = User(username="ikiru993", sex="M", email="ikiru9099@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        cls.user1.save()
        # Creating a conversation with the user id
        cls.conversation = Conversation(sender_id=cls.user.id, receiver_id=cls.user1.id)
        cls.conversation.save()
        cls.message = Message(content="He abuse me", user_id=cls.user.id, conversation_id=cls.conversation.id)
        cls.message.save()
        cls.reportedmessage = ReportedMessage(content="racism", reporting_user=cls.user.id, message_id=cls.message.id)
        cls.reportedmessage.save()
        
    
    @classmethod    
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.user.delete()
        cls.user1.delete()
        cls.message.delete()
        cls.reportedmessage.delete()
        storage.save()


    def test_reported_message_pep8_style(self):
        """test pycodestyle of reported_message model"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/reported_message.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(ReportedMessage.__doc__, None,
                          "reported_message.py needs docstring")
         self.assertTrue(len(ReportedMessage.__doc__) >= 1,
                         "reported_message.py needs a docstring")


    def test_reported_message_method_docstring(self):
        """check docstring for comment class methods"""
        for method in self.rmessagemethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)
    
    
    def test_reported_post_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reportedmessage, "id"))
        self.assertTrue(hasattr(self.reportedmessage, "created_at"))
        self.assertFalse(self.reportedmessage.id == None)
        self.assertFalse(self.reportedmessage.created_at == None)


    def test_reported_post_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reportedmessage, "content"))
        self.assertTrue(hasattr(self.reportedmessage, "reporting_user"))
        self.assertTrue(hasattr(self.reportedmessage, "message_id"))
        self.assertTrue(hasattr(self.reportedmessage, "is_resolved"))
        self.assertFalse(self.reportedmessage.message_id == None)
        self.assertFalse(self.reportedmessage.reporting_user == None)
        self.assertTrue(ReportedMessage.is_resolved.expression.default.arg == False)
        
        
    def test_repoted_post_methods(self):
        """test reported_post inherited method"""
        m_dict = self.reportedmessage.to_dict()
        self.assertEqual(type(m_dict), dict)
        self.assertFalse("_sa_instance_state" in m_dict)
        self.assertTrue("__class__" in m_dict)
 
        # Test the attribute value types
        self.assertEqual(self.reportedmessage.__class__.__name__, "ReportedMessage")
        self.assertEqual(type(self.reportedmessage.id), str)
        self.assertEqual(type(self.reportedmessage.created_at), datetime)
        self.assertEqual(type(self.reportedmessage.reporting_user), str)
        self.assertEqual(type(self.reportedmessage.content), str)
        self.assertEqual(type(self.reportedmessage.message_id), str)
        self.assertEqual(ReportedMessage.is_resolved.expression.type.python_type, bool)
