#!/usr/bin/python3
"""test base model"""
from datetime import date, datetime
import inspect
import pep8
import re
import unittest
from models.base_model2 import BaseModel2


pttn = "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
class testBaseModel2Doc(unittest.TestCase):
    """Test the doc and style of BaseModel2 class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.basemodel2methods = inspect.getmembers(
            BaseModel2, inspect.isfunction)
        cls.basemodel2 = BaseModel2()
  
    @classmethod   
    def tearDownClass(cls):
        """delete class instance use for the test"""
        del cls.basemodel2


    def test_basemodel2_pep8_style(self):
        """test pycodestyle of basemodel2 and test_basemodel2 models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/base_model2.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the basemodel2 model docstring"""
         self.assertIsNot(BaseModel2.__doc__, None,
                          "base_model2.py needs docstring")
         self.assertTrue(len(BaseModel2.__doc__) >= 1,
                         "base_model2.py needs a docstring")


    def test_basemodel2_method_docstring(self):
        """check docstring for basemodel2 class methods"""
        for method in self.basemodel2methods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)


    def test_basemodel2_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.basemodel2, "id"))
        self.assertTrue(hasattr(self.basemodel2, "created_at"))
        self.assertFalse(self.basemodel2.id == None)
        self.assertFalse(self.basemodel2.created_at == None)


    def test_basemodel2_methods(self):
        """test basemodel2 inherited method"""
        u_dict = self.basemodel2.to_dict()
        self.assertEqual(type(u_dict), dict)
        self.assertFalse("_sa_instance_state" in u_dict)
        self.assertTrue("__class__" in u_dict)

        # Test the type of the attribute
        self.assertEqual(self.basemodel2.__class__.__name__, "BaseModel2")
        self.assertEqual(type(self.basemodel2.id), str)
        self.assertEqual(type(self.basemodel2.created_at), datetime)


    def test_attribute_values(self):
        """Test the attribute values and format
        """
        self.assertTrue(bool(re.match(pttn, self.basemodel2.id)))
        
        
    def test_to_dict_method(self):
        """Test the to dict method"""
        to_dict = self.basemodel2.to_dict()
        self.assertIsInstance(to_dict, dict)
        self.assertNotIn("_sa_instance_state", to_dict)
        self.assertIn("__class__", to_dict)
        for key in to_dict:
            self.assertTrue(hasattr(self.basemodel2, key))
        self.assertEqual(to_dict["__class__"], "BaseModel2")
        
        self.assertTrue(bool(re.match(pattern, to_dict["id"])))
        try:
            created_type = datetime.fromisoformat(to_dict["created_at"])
        except ValueError:
            self.fail("Either created_at and/or updated_at \
                      is not datetime object format in to dict method")
        self.assertIsInstance(created_type, datetime)
