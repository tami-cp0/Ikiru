#!/usr/bin/python3
"""test base model"""
from datetime import date, datetime
import inspect
import pep8
import re
import unittest
from models import storage
from models.engine.db_storage import DBStorage


class testDBStorageDoc(unittest.TestCase):
    """Test the doc and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.dbstoragemethods = inspect.getmembers(
            DBStorage, inspect.isfunction)
        cls.dbstorage = DBStorage()
        cls.dbstorage.save()
  
    @classmethod   
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.dbstorage.delete()
        storage.save()


    def test_dbstorage_pep8_style(self):
        """test pycodestyle of dbstorage and test_dbstorage models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the dbstorage model docstring"""
         self.assertIsNot(DBStorage.__doc__, None,
                          "base_model.py needs docstring")
         self.assertTrue(len(DBStorage.__doc__) >= 1,
                         "base_model.py needs a docstring")


    def test_dbstorage_method_docstring(self):
        """check docstring for dbstorage class methods"""
        for method in self.dbstoragemethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)