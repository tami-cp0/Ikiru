#!/usr/bin/python3
"""test base model"""
from datetime import date, datetime
import inspect
import MySQLdb
import pep8
import unittest
from models import storage
from models.engine.db_storage import DBStorage
from models.user import User
from models.post import Post
from models.comment import Comment
from fabric.api import local


class testDBStorageDoc(unittest.TestCase):
    """Test the doc and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.dbstoragemethods = inspect.getmembers(
            DBStorage, inspect.isfunction)
        cls.dbstorage = DBStorage()
        cls.conn = MySQLdb.connect(
            host='localhost',
            user='ikiru_user',
            passwd='password',
            port=3306,
            db='ikiru_dev_db',
            charset='utf8')
        cls.pen = cls.conn.cursor()
        cls.pen.execute("DROP DATABASE IF EXISTS ikiru_dev_db")
        cls.pen.execute("CREATE DATABASE IF NOT EXISTS ikiru_dev_db")
        local('echo "quit" | ./console.py')
        


    @classmethod   
    def tearDownClass(cls):
        """delete class instance use for the test"""
        cls.conn.close()
        del cls.dbstorage

    def test_dbstorage_pep8_style(self):
        """test pycodestyle of dbstorage and test_dbstorage models"""
        pep8style = pep8.StyleGuide(quite=True)
        test = pep8style.check_files(["models/engine/db_storage.py"])
        self.assertEqual(test.total_errors, 0)
    def test_module_docstring(self):
         """Test the dbstorage model docstring"""
         self.assertIsNot(DBStorage.__doc__, None,
                          "db_storage.py needs docstring")
         self.assertTrue(len(DBStorage.__doc__) >= 1,
                         "db_storage.py needs a docstring")


    def test_dbstorage_method_docstring(self):
        """check docstring for dbstorage class methods"""
        for method in self.dbstoragemethods:
            self.assertIsNot(method[1].__doc__, None)
            self.assertTrue(len(method[1].__doc__) >= 1)
            
            
    def test_the_db_is_empty(self):
        """Test to ensure the db is empty"""
        pass        
            
            
    def test_new_save_and_delete_methods(self):
        """Test the new, save and delete method"""
        user= User(username="ikiru8db", sex="M", email="ikiru8db@ikiru.com", name="Ikiru", dob='2000-04-10', password="ikiru", bio="ask me")
        user.save()
        #query = "SELECT * FROM user WHERE username = {s}"
        self.pen.execute(f"""
                         SELECT * FROM users WHERE username = {user.username}
                         """)
        user_cp = self.pen.fetchone()
        self.assertEqual(self.pen.rowcount, 1)
        user_attr_list = [attr for attr in user_cp]
        #user1 = User(username="ikiru9i9db", sex="M", email="ikiru900db9@ikiru.com", name="Ikiru", dob='2000-04-10', password="ikiru",bio="ask me")
        #user1.save()
        self.assertIn(user.id, user_attr_list)
        user_dict = user.to_dict()
        self.assertIn(user_dict["updated_at"], user_attr_list)
        self.assertIn(user_dict["created_at"], user_attr_list)
        self.assertIn(user_dict["email"], user_attr_list)
        self.assertIn(user_dict["sex"], user_attr_list)
        self.assertIn(user_dict["dob"], user_attr_list)
        self.assertIn(user_dict["bio"], user_attr_list)
