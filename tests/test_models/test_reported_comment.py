#!/usr/bin/python3
"""test message model"""
from datetime import date
import inspect
import pep8
import unittest
from models import storage
from models.comment import Comment
from models.post import Post
from models.reported_comment import ReportedComment
from models.user import User


class testPostDoc(unittest.TestCase):
    """Test the doc and style of reported_comment class"""
    def setUp(self):
        """set up class instance for test"""
        self.user = User(username="ikiru", sex="M", email="ikiru@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        self.user.save()
        self.post = Post(content="He abuse me", user_id=self.user.id)
        self.post.save()
        self.comment = Comment(content="He abuse me", user_id=self.user.id, post_id=self.post.id)
        self.comment.save()
        self.reportedcomment = ReportedComment(content="racism", reporting_user=self.user.id, comment_id=self.comment.id)
        self.reportedcomment.save()


    def tearDown(self):
        """delete class instance use for the test"""
        self.user.delete()
        self.post.delete()
        self.comment.delete()
        self.reportedcomment.delete()
        storage.save()


    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.rcommentmethods = inspect.getmembers(ReportedComment, inspect.isfunction)


    def test_reported_comment_pep8_style(self):
        """test pycodestyle of reported_comment and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/reported_comment.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(ReportedComment.__doc__, None,
                          "reported_comment.py needs docstring")
         self.assertTrue(len(ReportedComment.__doc__) >= 1,
                         "reported_comment.py needs a docstring")


    def test_reported_comment_method_docstring(self):
        """check docstring for comment class methods"""
        for method in self.rcommentmethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)
    
    
    def test_reported_post_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reportedcomment, "id"))
        self.assertTrue(hasattr(self.reportedcomment, "created_at"))
        self.assertFalse(self.reportedcomment.id == None)
        self.assertFalse(self.reportedcomment.created_at == None)


    def test_reported_post_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reportedcomment, "content"))
        self.assertTrue(hasattr(self.reportedcomment, "reporting_user"))
        self.assertTrue(hasattr(self.reportedcomment, "comment_id"))
        self.assertTrue(hasattr(self.reportedcomment, "is_resolved"))
        self.assertFalse(self.reportedcomment.comment_id == None)
        self.assertFalse(self.reportedcomment.reporting_user == None)
        self.assertTrue(ReportedComment.is_resolved.expression.default.arg == False)
        
        
    def test_repoted_post_methods(self):
        """test reported_post inherited method"""
        m_dict = self.reportedcomment.to_dict()
        self.assertEqual(type(m_dict), dict)
        self.assertFalse("_sa_instance_state" in m_dict)
        self.assertTrue("__class__" in m_dict)
        # Test the dict attribute
        for attr in m_dict.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in m_dict)

        # Test the attribute value types
        self.assertEqual(self.reportedcomment.__class__, "ReportedComment")
        self.assertEqul(type(self.reportedcomment.id), str)
        self.assertEqul(type(self.reportedcomment.created_at), str)
        self.assertEqul(type(self.reportedcomment.reporting_user), str)
        self.assertEqul(type(self.reportedcomment.content), str)
        self.assertEqul(type(self.reportedcomment.comment_id), str)
        self.assertEqual(ReportedComment.is_resolved.expression.type.python_type, bool)
