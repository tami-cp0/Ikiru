#!/usr/bin/python3
"""test message model"""
from datetime import date, datetime
import inspect
import pep8
import unittest
from models import storage
from models.post import Post
from models.user import User


class testPostDoc(unittest.TestCase):
    """Test the doc and style of Message class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.postmethods = inspect.getmembers(Post, inspect.isfunction)
        cls.user = User(username="ikiru7", sex="M", email="ikiru7@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        cls.user.save()
        cls.post = Post(content="He abuse me", user_id=self.user.id)
        cls.post.save()
        
    
    @classmethod
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.user.delete()
        cls.post.delete()
        storage.save()


    def test_user_pep8_style(self):
        """test pycodestyle of user and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/post.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(Post.__doc__, None,
                          "post.py needs docstring")
         self.assertTrue(len(Post.__doc__) >= 1,
                         "post.py needs a docstring")


    def test_user_method_docstring(self):
        """check docstring for user class methods"""
        for method in self.postmethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)
    
    
    def test_message_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.post, "id"))
        self.assertTrue(hasattr(self.post, "created_at"))
        self.assertTrue(hasattr(self.post, "updated_at"))
        self.assertFalse(self.post.id == None)
        self.assertFalse(self.post.created_at == None)
        self.assertFalse(self.post.updated_at == None)
        self.assertTrue(Post.is_reported.expression.default.arg == False)
        self.assertTrue(Post.is_anonymous.expression.default.arg == False)


    def test_message_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.post, "content"))
        self.assertTrue(hasattr(self.post, "user_id"))
        self.assertFalse(self.post.user_id == None) 
        
        
    def test_message_methods(self):
        """test message inherited method"""
        m_dict = self.post.to_dict()
        self.assertEqual(type(m_dict), dict)
        self.assertFalse("_sa_instance_state" in m_dict)
        self.assertTrue("__class__" in m_dict)

        # Test the attribute value types
        self.assertEqual(self.post.__class__.__name__, "Post")
        self.assertEqul(type(self.post.id), str)
        self.assertEqul(type(self.post.created_at), str) 
        self.assertEqul(type(self.post.user_id), str)
        self.assertEqual(Post.is_anonymous.expression.type.python_type, bool)
        self.assertEqual(Post.is_reported.expression.type.python_type, bool)
