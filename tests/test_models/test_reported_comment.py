#!/usr/bin/python3
"""test reported_comment model"""
from datetime import date, datetime
import inspect
import pep8
import unittest
from models import storage
from models.comment import Comment
from models.post import Post
from models.reported_comment import ReportedComment
from models.user import User


class testReportedCommentDoc(unittest.TestCase):
    """Test the doc and style of reported_comment class"""
    def setUp(self):
        """set up class instance for test"""
        

    

    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.rcommentmethods = inspect.getmembers(ReportedComment,
                                                 inspect.isfunction)
        cls.user = User(username="ikiru6", sex="M", email="ikiru6@ikiru.com",
                        name="Ikiru", dob='2000-04-10', password="ikiru")
        cls.user.save()
        cls.post = Post(content="He abuse me", user_id=cls.user.id)
        cls.post.save()
        cls.comment = Comment(content="He abuse me", user_id=cls.user.id,
                              post_id=cls.post.id)
        cls.comment.save()
        cls.reportedcomment = ReportedComment(content="racism",
                                              reporting_user=cls.user.id,
                                              comment_id=cls.comment.id)
        cls.reportedcomment.save()

    
    @classmethod    
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.user.delete()
        cls.post.delete()
        cls.comment.delete()
        cls.reportedcomment.delete()
        storage.save()


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


    def test_reported_comment_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reportedcomment, "id"))
        self.assertTrue(hasattr(self.reportedcomment, "created_at"))
        self.assertFalse(self.reportedcomment.id == None)
        self.assertFalse(self.reportedcomment.created_at == None)


    def test_reported_comment_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reportedcomment, "content"))
        self.assertTrue(hasattr(self.reportedcomment, "reporting_user"))
        self.assertTrue(hasattr(self.reportedcomment, "comment_id"))
        self.assertTrue(hasattr(self.reportedcomment, "is_resolved"))
        self.assertFalse(self.reportedcomment.comment_id == None)
        self.assertFalse(self.reportedcomment.reporting_user == None)
        self.assertTrue(
                ReportedComment.is_resolved.expression.default.arg == False)


    def test_repoted_comment_methods(self):
        """test reported_comment inherited method"""
        m_dict = self.reportedcomment.to_dict()
        self.assertEqual(type(m_dict), dict)
        self.assertFalse("_sa_instance_state" in m_dict)
        self.assertTrue("__class__" in m_dict)

        # Test the attribute value types
        self.assertEqual(
                self.reportedcomment.__class__.__name__, "ReportedComment")
        self.assertEqual(type(self.reportedcomment.id), str)
        self.assertEqual(type(self.reportedcomment.created_at), datetime)
        self.assertEqual(type(self.reportedcomment.reporting_user), str)
        self.assertEqual(type(self.reportedcomment.content), str)
        self.assertEqual(type(self.reportedcomment.comment_id), str)
        self.assertEqual(
                ReportedComment.is_resolved.expression.type.python_type, bool)
