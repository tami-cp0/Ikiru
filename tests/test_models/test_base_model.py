#!/usr/bin/python3
"""test base model"""
from datetime import date, datetime
import inspect
import pep8
import re
import unittest
from models import storage
from models.base_model import BaseModel


class testBaseModelDoc(unittest.TestCase):
    """Test the doc and style of BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.basemodelmethods = inspect.getmembers(
            BaseModel, inspect.isfunction)
        cls.basemodel = BaseModel()
        cls.basemodel.save()
  
    @classmethod   
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.basemodel.delete()
        storage.save()


    def test_basemodel_pep8_style(self):
        """test pycodestyle of basemodel and test_basemodel models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the basemodel model docstring"""
         self.assertIsNot(BaseModel.__doc__, None,
                          "base_model.py needs docstring")
         self.assertTrue(len(BaseModel.__doc__) >= 1,
                         "base_model.py needs a docstring")


    def test_basemodel_method_docstring(self):
        """check docstring for basemodel class methods"""
        for method in self.basemodelmethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)


    def test_basemodel_class_attr(self):
        """test the super class attributes"""
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertFalse(self.basemodel.id == None)
        self.assertFalse(self.basemodel.created_at == None)
        self.assertFalse(self.basemodel.updated_at == None)


    def test_basemodel_methods(self):
        """test basemodel inherited method"""
        u_dict = self.basemodel.to_dict()
        self.assertEqual(type(u_dict), dict)
        self.assertFalse("_sa_instance_state" in u_dict)
        self.assertTrue("__class__" in u_dict)

        # Test the type of the attribute
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")
        self.assertEqual(type(self.basemodel.id), str)
        self.assertEqual(type(self.basemodel.created_at), datetime)
        self.assertEqual(type(self.basemodel.updated_at), datetime)


    def test_basemodel_save_and_delete_methods(self):
        """Test basemodel save and delete methods"""
        basemodel = self.basemodel = BaseModel()
        basemodel.save()
        #Testt save method
        basemodel_copy = storage.get(BaseModel, basemodel.id)
        self.assertEqual(basemodel_copy, basemodel)
        self.assertEqual(basemodel_copy.id, basemodel.id)

        # test the delete method
        basemodel_copy.delete()
        storage.save()
        self.assertEqual(storage.get(BaseModel,  basemodel.id), None)


    def test_attribute_values(self):
        """Test the attribute values and format
        """
        pattern = "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]\
            {3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
        self.assertTrue(bool(re.match(pattern, self.basemodel.id)))
        try:
            created_type = datetime.fromisoformat(self.basemodel.created_at)
            updated_type = datetime.fromisoformat(self.basemodel.updated_at)
        except ValueError:
            self.fail("Either created_at and/or \
                updated_at is not datetime object format")
        self.assertIsInstance(created_type, datetime)
        self.assertIsInstance(updated_type, datetime)
        
        
    def test_to_dict_method(self):
        """Test the to dict method"""
        to_dict = self.basemodel.to_dict()
        self.assertIsInstance(to_dict, dict)
        self.assertNotIn("_sa_instance_state", to_dict)
        self.assertNIn("__class__", to_dict)
        for key in to_dict:
            self.assertTrue(hasattr(self.basemodel, key))
        self.assertEqual(to_dict["__class__"], "BaseModel")
        
        pattern = "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]\
        {3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
        self.assertTrue(bool(re.match(pattern, to_dict["id"])))
        try:
            created_type = datetime.fromisoformat(to_dict["created_at"])
            updated_type = datetime.fromisoformat(to_dict["updated_at"])
        except ValueError:
            self.fail("Either created_at and/or updated_at \
                      is not datetime object format in to dict method")
        self.assertIsInstance(created_type, datetime)
        self.assertIsInstance(updated_type, datetime)
