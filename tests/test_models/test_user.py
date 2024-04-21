#!/usr/bin/python3
"""test message model"""
from datetime import date
import inspect
import pep8
import unittest
from models import storage
from models.user import User


class testMessageDoc(unittest.TestCase):
    """Test the doc and style of Message class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.usermethods = inspect.getmembers(User, inspect.isfunction)
        cls.user = User(
            username="ikiru1", sex="M", email="ikiru1@ikiru.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru", bio="i live here")
        cls.user.save()
  
    @classmethod   
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.user.delete()
        storage.save()


    def test_user_pep8_style(self):
        """test pycodestyle of user and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/user.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(User.__doc__, None,
                          "user.py needs docstring")
         self.assertTrue(len(User.__doc__) >= 1,
                         "user.py needs a docstring")


    def test_user_method_docstring(self):
        """check docstring for user class methods"""
        for method in self.usermethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)


    def test_user_super_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertFalse(self.user.id == None)
        self.assertFalse(self.user.created_at == None)
        self.assertFalse(self.user.updated_at == None)


    def test_user_class_attr(self):
        """test the super class attributes"""
        # test the if the class instance has the class attribute
        self.assertTrue(hasattr(self.user, "username"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "sex"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "dob"))
        self.assertTrue(hasattr(self.user, "is_active"))
        self.assertTrue(hasattr(self.user, "is_admin"))
        self.assertTrue(hasattr(self.user, "name"))
        self.assertTrue(hasattr(self.user, "is_reported"))
        self.assertTrue(hasattr(self.user, "bio"))

        #Test the attribute values
        self.assertTrue(self.user.id != None)
        self.assertTrue(self.user.created_at != None)
        self.assertTrue(self.user.updated_at != None)
        self.assertTrue(self.user.name != None)
        self.assertTrue(self.user.bio != None)
        self.assertTrue(self.user.sex != None)
        self.assertTrue(self.user.email != None)
        self.assertTrue(self.user.password != None)
        self.assertTrue(self.user.dob != None)
        self.assertTrue(self.user.username != None)
        self.assertTrue(User.is_active.expression.default.arg == False)
        self.assertTrue(User.is_admin.expression.default.arg == False)
        self.assertTrue(User.is_reported.expression.default.arg == False)


    def test_user_methods(self):
        """test user inherited method"""
        u_dict = self.user.to_dict()
        self.assertEqual(type(u_dict), dict)
        self.assertFalse("_sa_instance_state" in u_dict)
        self.assertTrue("__class__" in u_dict)

        # Test the type of the attribute
        self.assertEqual(self.user.__class__, "User")
        self.assertEqul(type(self.user.id), str)
        self.assertEqul(type(self.user.created_at), str)
        self.assertEqul(type(self.user.updated_at), str)
        self.assertEqul(type(self.user.username), str)
        self.assertEqul(type(self.user.email), str)
        self.assertEqul(type(self.user.sex), str)
        self.assertEqul(type(self.user.password), str)
        self.assertEquall(type(self.user.dob), date)
        # Test the class defaut type
        self.assertEqul(User.is_active.expression.type.python_type, bool)
        self.assertEqul(User.is_admin.expression.type.python_type, bool)
        self.assertEqul(User.is_reported.expression.type.python_type, bool)
        self.assertEqul(
                User.is_active.expression.type.python_type, bool)
        self.assertEqul(type(self.user.name), str)
        self.assertEqul(type(self.user.bio), str)


    def test_user_save_and_delete_methods(self):
        """Test user save and delete methods"""
        user = self.user = User(
                username ="ikirujunior", sex="M", email="ikiru67@ikiru.com",
                name="Ikiru junior", dob=date(2000, 4, 10), password="ikiru")
        user.save()
        #Testt save method
        user_copy = storage.get(User, user.id)
        self.assertEqual(user_copy, user)
        self.assertEqual(user_copy.id, user.id)
        self.assertEqual(user_copy.name, user.name)
        self.assertEqual(user_copy.username, user.username)
        # test the delete method
        user_copy.delete()
        storage.save()
        self.assertEqual(storage.get(User, user.id), None)
