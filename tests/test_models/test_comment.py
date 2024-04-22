#!/usr/bin/python3
"""test comment model"""
from datetime import date, datetime
import inspect
import pep8
import unittest
from models import storage
from models.comment import Comment
from models.post import Post
from models.user import User


class testCommentDoc(unittest.TestCase):
    """Test the doc and style of Message class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.commentmethods = inspect.getmembers(Comment, inspect.isfunction)
        cls.user = User(username="ikiru7", sex="M", email="ikiru7@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        cls.user.save()
        cls.post = Post(content="He abuse me", user_id=cls.user.id)
        cls.post.save()
        cls.comment = Comment(content="He abuse me", user_id=cls.user.id, post_id=cls.post.id)
        cls.comment.save()
        
        
    @classmethod
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.user.delete()
        cls.post.delete()
        cls.comment.delete()
        storage.save()


    def test_user_pep8_style(self):
        """test pycodestyle of user and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/comment.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(Comment.__doc__, None,
                          "comment.py needs docstring")
         self.assertTrue(len(Comment.__doc__) >= 1,
                         "comment.py needs a docstring")


    def test_user_method_docstring(self):
        """check docstring for user class methods"""
        for method in self.commentmethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)
    
    
    def test_comment_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.comment, "id"))
        self.assertTrue(hasattr(self.comment, "created_at"))
        self.assertTrue(hasattr(self.comment, "updated_at"))
        self.assertFalse(self.comment.id == None)
        self.assertFalse(self.comment.created_at == None)
        self.assertFalse(self.comment.updated_at == None)
        self.assertTrue(Comment.is_reported.expression.default.arg == False)
        self.assertTrue(Comment.is_anonymous.expression.default.arg == False)


    def test_comment_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.comment, "content"))
        self.assertTrue(hasattr(self.comment, "user_id"))
        self.assertFalse(self.comment.user_id == None) 
        
        
    def test_comment_methods(self):
        """test comment inherited method"""
        m_dict = self.comment.to_dict()
        self.assertEqual(type(m_dict), dict)
        self.assertFalse("_sa_instance_state" in m_dict)
        self.assertTrue("__class__" in m_dict)
 
        # Test the attribute value types
        self.assertEqual(self.comment.__class__.__name__, "Comment")
        self.assertEqual(type(self.comment.id), str)
        self.assertEqual(type(self.comment.created_at), datetime)
        self.assertEqual(type(self.comment.updated_at), datetime)
        self.assertEqual(type(self.comment.user_id), str)
        self.assertEqual(Comment.is_anonymous.expression.type.python_type, bool)
        self.assertEqual(Comment.is_reported.expression.type.python_type, bool)
