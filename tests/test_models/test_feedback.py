#!/usr/bin/python3
"""test message model"""
from datetime import date, datetime
import inspect
import pep8
import unittest
from models import storage
from models.feedback import Feedback
from models.user import User


class testFeedbackDoc(unittest.TestCase):
    """Test the doc and style of Message class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.feedbackmethods = inspect.getmembers(Feedback, inspect.isfunction)
        cls.user = User(username="ikiru7", sex="M", email="ikiru7@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        cls.user.save()
        cls.feedback = Feedback(content="He abuse me", user_id=self.user.id)
        cls.feedback.save()


    @classmethod
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.user.delete()
        cls.feedback.delete()
        storage.save()


    def test_user_pep8_style(self):
        """test pycodestyle of user and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/feedback.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(Feedback.__doc__, None,
                          "feedback.py needs docstring")
         self.assertTrue(len(Feedback.__doc__) >= 1,
                         "feedback.py needs a docstring")


    def test_user_method_docstring(self):
        """check docstring for user class methods"""
        for method in self.feedbackmethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)
    
    
    def test_message_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.feedback, "id"))
        self.assertTrue(hasattr(self.feedback, "created_at"))
        self.assertFalse(self.feedback.id == None)
        self.assertFalse(self.feedback.created_at == None)


    def test_message_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.feedback, "content"))
        self.assertTrue(hasattr(self.feedback, "user_id"))
        self.assertFalse(self.feedback.user_id == None) 
        
        
    def test_message_methods(self):
        """test message inherited method"""
        m_dict = self.feedback.to_dict()
        self.assertEqual(type(m_dict), dict)
        self.assertFalse("_sa_instance_state" in m_dict)
        self.assertTrue("__class__" in m_dict)

        # Test the attribute value types
        self.assertEqual(self.feedback.__class__, "Feedback")
        self.assertEqul(type(self.feedback.id), str)
        self.assertEqul(type(self.feedback.created_at), str) 
        self.assertEqul(type(self.feedback.user_id), str)
