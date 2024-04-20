#!/usr/bin/python3
"""test message model"""
from datetime import date
import inspect
import pep8
import unittest
from models import storage
from models.message import Message
from models.reported_message import ReportedMessage
from models.user import User


class testMessageDoc(unittest.TestCase):
    """Test the doc and style of reported_message class"""
    def setUp(self):
        """set up class instance for test"""
        self.user = User(username="ikiru", sex="M", email="ikiru@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        self.user.save()
        self.message = Message(content="He abuse me", user_id=self.user.id)
        self.message.save()
        self.reportedmessage = ReportedMessage(content="racism", reporting_user=self.user.id, message_id=self.message.id)
        self.reportedmessage.save()


    def tearDown(self):
        """delete class instance use for the test"""
        self.user.delete()
        self.message.delete()
        self.reportedmessage.delete()
        storage.save()


    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.rmessagemethods = inspect.getmembers(ReportedMessage, inspect.isfunction)


    def test_reported_message_pep8_style(self):
        """test pycodestyle of reported_message model"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/reported_message.py"])
        self.assertEqual(test.total_errors, 0,
                         f"pycodestyle error in {test.filename}")
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(ReportedMessage.__doc__, None,
                          "reported_message.py needs docstring")
         self.assertTrue(len(ReportedMessage.__doc__) >= 1,
                         "reported_message.py needs a docstring")


    def test_reported_message_method_docstring(self):
        """check docstring for comment class methods"""
        for method in self.rmessagemethods:
            self.assertIsNot(method[1].__doc__, None, f"{method[0]} in
                             {inspect.getfiles(ReportedMessage)} needs a docstring")
            self.assertTrue(len(method[1].__doc__) >= 1, f"{method[0]} in
            {inspect.getfiles(ReportedMessage)} needs a docstring")
    
    
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
        # Test the dict attribute
        for attr in m_dict.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in m_dict)

        # Test the attribute value types
        self.assertEqual(self.reportedmessage.__class__, "ReportedMessage")
        self.assertEqul(type(self.reportedmessage.id), str)
        self.assertEqul(type(self.reportedmessage.created_at), str)
        self.assertEqul(type(self.reportedmessage.reporting_user), str)
        self.assertEqul(type(self.reportedmessage.content), str)
        self.assertEqul(type(self.reportedmessage.message_id), str)
        self.assertEqual(ReportedMessage.is_resolved.expression.type.python_type, bool)
