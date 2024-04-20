#!/usr/bin/python3
"""test message model"""
from datetime import date, datetime
import inspect
import pep8
import unittest
from models import storage
from models.reported_user import ReportedUser
from models.user import User


class testReportedUserDoc(unittest.TestCase):
    """Test the doc and style of Message class"""
    def setUp(self):
        """set up class instance for test"""
        self.user = User(username="ikiru", sex="M", email="ikiru@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru")
        self.user.save()
        self.reporteduser = ReportedUser(content="He abuse me", user_id=self.user.id)
        self.reporteduser.save()


    def tearDown(self):
        """delete class instance use for the test"""
        self.user.delete()
        self.reporteduser.delete()
        storage.save()


    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.rusermethods = inspect.getmembers(ReportedUser, inspect.isfunction)


    def test_user_pep8_style(self):
        """test pycodestyle of user and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/reported_user.py"])
        self.assertEqual(test.total_errors, 0,
                         f"pycodestyle error in {test.filename}")
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(ReportedUser.__doc__, None,
                          "reported_user.py needs docstring")
         self.assertTrue(len(ReportedUser.__doc__) >= 1,
                         "reported_user.py needs a docstring")


    def test_user_method_docstring(self):
        """check docstring for user class methods"""
        for method in self.rusermethods:
            self.assertIsNot(method[1].__doc__, None, f"{method[0]} in
                             {inspect.getfiles(ReportedUser)} needs a docstring")
            self.assertTrue(len(method[1].__doc__) >= 1, f"{method[0]} in
            {inspect.getfiles(ReportedUser)} needs a docstring")
    
     
    def test_message_super_class_attr(self):
        """test the super class attributes"""
        
        self.assertTrue(hasattr(self.reporteduser, "id"))
        self.assertTrue(hasattr(self.reporteduser, "created_at"))
        self.assertTrue(hasattr(self.reporteduser, "updated_at"))
        self.assertFalse(self.reporteduser.id == None)
        self.assertFalse(self.reporteduser.created_at == None)


    def test_message_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.reporteduser, "content"))
        self.assertTrue(hasattr(self.reporteduser, "is_reported"))
        self.assertTrue(hasattr(self.reporteduser, "user_id"))
        self.assertFalse(self.reporteduser.user_id == None)
        self.assertFalse(self.reporteduser.is_resolved == None)
        
        
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
        self.assertEqual(self.reporteduser.__class__, "Conversation")
        self.assertEqul(type(self.reporteduser.id), str)
        self.assertEqul(type(self.reporteduser.created_at), str)
        self.assertEqul(type(self.reporteduser.is_resolved), str)
        self.assertEqul(type(self.reporteduser.user_id), str)
        self.assertEqual(ReportedUser.is_resolved.expression.type.python_type, bool)


    def message_save_and_delete_methods(self):
        """Test message save and delete methods"""
        user = self.user = User(
                username ="ikirujunior", sex="M", email="ikiru@ikiru.com",
                name="Ikiru junior", dob=date(2000, 4, 10), password="ikiru")
        user.save()
        reporteduser= ReportedUser(content="Good", user_id=self.user.id)

        reporteduser.save()
        #Testt save method
        reporteduser_copy = storage.get(ReportedUser, reporteduser.id)
        self.assertEqual(reporteduser_copy, reporteduser)
        self.assertEqual(reporteduser_copy.id, reporteduser.id)
        self.assertEqual(reporteduser_copy.user_d, reporteduser.user_id)
        # test the delete method
        reporteduser_copy.delete()
        storage.save()
        self.assertEqual(storage.get(ReportedUser, reporteduser.id), None)