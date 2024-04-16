#!/usr/bin/python3
"""test message model"""
from datetime import datetime
import inspect
import pep8
import unitest
from models.user import User


class testMessageDoc(unitest.TestCase):
    """Test the doc and style of Message class"""
    def setUp(self):
        """set up class instance for test"""
        self.user = User(username="ikiru", sex="M", email="ikiru@ikiru.com", name="Ikiru", dob="", password="ikiru")


    def tearDown(self):
        """delete class instance use for the test"""
        del self.user


    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.usermethods = inspect.getmembers(User, inspect.isfunction)


    def test_user_pep8_style(self):
        """test pycodestyle of user and test_user models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/user"])
        self.assertEqual(test.total_errors, 0,
                         f"pycodestyle error in {test.filename}")
    def test_module_docstring(self):
         """Test the user model docstring"""
         self.assertIsNot(User.__doc__, None,
                          "user.py needs docstring")
         self.assertTrue(len(User.__doc__) >= 1,
                         "user.py needs a docstring")


    def test_user_method_docstring(self):
        """check docstring for user class methods"""
        for method in self.usermethod:
            self.assertIsNot(method[1].__doc__, None, f"{method[0]} in
                             {inspect.getfiles(User)} needs a docstring")
            self.assertTrue(len(method[1].__doc__) >= 1, f"{method[0]} in
            {inspect.getfiles(User)} needs a docstring")


class testUser(unitest.TestCase):
    """Test the attributes and methods of the user class"""
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
        self.assertTrue(hasattr(user, "username"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "sex"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "dob"))
        self.assertTrue(hasattr(user, "is_active"))
        self.assertTrue(hasattr(user, "is_admin"))
        self.assertTrue(hasattr(user, "name"))
        self.assertTrue(hasattr(user, "is_reported"))
        self.assertTrue(hasattr(user, "bio"))

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
        self.assertTrue(self.user.is_admin == False)
        self.assertTrue(self.user.is_active == False)
        self.assertTrue(self.user.is_reportted == False)


    def test_user_methods(self):
        """test user inherited method"""
        u_dict = self.user.to_dict()
        self.assertEqual(type(u_dict), dict)
        self.assertFalse("_sa_instance_state" in u_dict)
        self.assertTrue("__class__" in u_dict)
        for attr in u_dict.__dict__:
            if attr not "_sa_instance_state":
                self.assertTrue(attr in u_dict)
        self.assertEqual(self.user.__class__, "User")
        self.assertEqul(type(self.user.id), str)
        self.assertEqul(type(self.user.created_at), str)
        self.assertEqul(type(self.user.updated_at), str)
        self.assertEqul(type(self.user.username), str)
        self.assertEqul(type(self.user.email), str)
        self.assertEqul(type(self.user.sex), str)
        self.assertEqul(type(self.user.password), str)
        self.assertEqul(type(self.user.is_active), bool)
        self.assertEqul(type(self.user.is_admin), bool)
        self.assertEqul(type(self.user.is_reported), bool)
        self.assertEqul(type(self.user.dob), bool)
        self.assertEqul(type(self.user.name), str))
        self.assertEqul(type(self.user.bio), str)
