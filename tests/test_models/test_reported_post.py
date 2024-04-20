#!/usr/bin/python3
"""test message model"""
from datetime import date
import inspect
import pep8
import unittest
from models import storage
from models.post import Post
from models.reported_post import ReportedPost
from models.user import User


class testPostDoc(unittest.TestCase):
    """Test the doc and style of reported_post class"""
    def setUp(self):
        """set up class instance for test"""
        self.user = User(username="ikiru", sex="M", email="ikiru@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        self.user.save()
        self.reportedpost = Post(content="He abuse me", user_id=self.user.id)
        self.reportedpost.save()
        self.reportedpost = ReportedPost(content="racism", user_id=self.user.id, post_id=self.reportedpost.id)


    def tearDown(self):
        """delete class instance use for the test"""
        self.user.delete()
        self.reportedpost.delete()
        self.reportedpost.delete()
        storage.save()


    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.rpostmethods = inspect.getmembers(ReportedPost, inspect.isfunction)


    def test_reported_post_pep8_style(self):
        """test pycodestyle of reported_post and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/reported_post.py"])
        self.assertEqual(test.total_errors, 0,
                         f"pycodestyle error in {test.filename}")
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(ReportedPost.__doc__, None,
                          "reported_post.py needs docstring")
         self.assertTrue(len(ReportedPost.__doc__) >= 1,
                         "reported_post.py needs a docstring")


    def test_reported_post_method_docstring(self):
        """check docstring for reported_post class methods"""
        for method in self.rpostmethods:
            self.assertIsNot(method[1].__doc__, None, f"{method[0]} in
                             {inspect.getfiles(ReportedPost)} needs a docstring")
            self.assertTrue(len(method[1].__doc__) >= 1, f"{method[0]} in
            {inspect.getfiles(ReportedPost)} needs a docstring")
    
    
    def test_reported_post_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reportedpost, "id"))
        self.assertTrue(hasattr(self.reportedpost, "created_at"))
        self.assertTrue(hasattr(self.reportedpost, "updated_at"))
        self.assertFalse(self.reportedpost.id == None)
        self.assertFalse(self.reportedpost.created_at == None)
        self.assertFalse(self.reportedpost.updated_at == None)
        self.assertTrue(ReportedPost.is_resolved.expression.default.arg == False)


    def test_reported_post_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reportedpost, "content"))
        self.assertTrue(hasattr(self.reportedpost, "user_id"))
        self.assertFalse(self.reportedpost.user_id == None) 
        
        
    def test_repoted_post_methods(self):
        """test reported_post inherited method"""
        m_dict = self.reportedpost.to_dict()
        self.assertEqual(type(m_dict), dict)
        self.assertFalse("_sa_instance_state" in m_dict)
        self.assertTrue("__class__" in m_dict)
        # Test the dict attribute
        for attr in m_dict.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in m_dict)

        # Test the attribute value types
        self.assertEqual(self.reportedpost.__class__, "ReportedPost")
        self.assertEqul(type(self.reportedpost.id), str)
        self.assertEqul(type(self.reportedpost.created_at), str)
        self.assertEqul(type(self.reportedpost.post_id), str)
        self.assertEqul(type(self.reportedpost.user_id), str)
        self.assertEqual(ReportedPost.is_resolved.expression.type.python_type, bool)
