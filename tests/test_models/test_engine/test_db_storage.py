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
from fabric.api import local


class testDBStorageDoc(unittest.TestCase):
    """Test the doc and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for doc test"""
        cls.dbstoragemethods = inspect.getmembers(
            DBStorage, inspect.isfunction)
        cls.dbstorage = DBStorage()
        conn = MySQLdb.connect(
            host='localhost',
            user='ikiru_user',
            passwd='password',
            port=3306,
            db='ikiru_db',
            charset='utf8')
        pen = conn.cursor()
        pen.execute("DROP DATABASE IF EXISTS ikiru_db")
        pen.execute("CREATE DATABASE IF NOT EXISTS ikiru_db")
        pen.close()

        local('echo "quit" | ./console.py')
        


    @classmethod   
    def tearDownClass(cls):
        """delete class instance use for the test"""
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
            
            
    def db_connection(self):
        """Connect to db"""
        conn = MySQLdb.connect(
            host='localhost',
            user='ikiru_user',
            passwd='password',
            port=3306,
            db='ikiru_db',
            charset='utf8')
        return conn

            
    def test_new_save_and_delete_methods(self):
        """Test the new, save and delete method"""
        user= User(username="ikiru8db", sex="M", email="ikiru8db@ikiru.com", name="Ikiru", dob='2000-04-10', password="ikiru", bio="ask me")
        user.save()
        #query = "SELECT * FROM user WHERE username = {s}"
        pen = self.db_connection().cursor()
        pen.execute(f"""
                         SELECT * FROM users WHERE username = '{user.username}'
                         """)
        user_cp = pen.fetchone()
        self.assertEqual(pen.rowcount, 1)
        user_attr_list = [attr for attr in user_cp]
        #user1 = User(username="ikiru9i9db", sex="M", email="ikiru900db9@ikiru.com", name="Ikiru", dob='2000-04-10', password="ikiru",bio="ask me")
        #user1.save()
        # Test the dbstorage save and new methods
        self.assertIn(user.id, user_attr_list)
        self.assertIn(user.name, user_attr_list)
        self.assertIn(user.username, user_attr_list)
        self.assertIn(user.email, user_attr_list)
        self.assertIn(user.sex, user_attr_list)
        self.assertIn(user.dob, user_attr_list)
        self.assertIn(user.bio, user_attr_list)
        
        # Test Delete method
        user.delete()
        storage.save()
        pen.close()
        pen = self.db_connection().cursor()
        pen.execute(f"""
                    SELECT * FROM users WHERE username = '{user.username}';
                    """)
        user_cp = pen.fetchone()
        self.assertEqual(pen.rowcount, 0)
        pen.close()


    def test_count_and_get_methods(self):
        """"Test the count and get method of dbstorage"""
        user= User(username="ikiru8db1", sex="M", email="ikiru8d2b@ikiru.com", name="Ikiru", dob='2000-04-10', password="ikiru", bio="ask me")
        user.save()
        user1 = User(username="ikiru9i9db", sex="M", email="ikiru900db9@ikiru.com", name="Ikiru", dob='2000-04-10', password="ikiru",bio="ask me")
        user1.save()
        user2= User(username="ikiru8rdb1", sex="M", email="ikiru8d29b@ikiru.com", name="Ikiru", dob='2000-04-10', password="ikiru", bio="ask me")
        user2.save()
        user3 = User(username="ikiru9i9db6", sex="M", email="ikiru900d5b9@ikiru.com", name="Ikiru88", dob='2000-04-18', password="ikiru97",bio="you ask me")
        user3.save()
        pen = self.db_connection().cursor()
        pen.execute(f"""
                    SELECT * FROM users;
                    """)
        # Test count method
        self.assertEqual(pen.rowcount, storage.count(User))
        # Test get method
        pen = self.db_connection().cursor()
        pen.execute(f"""
                         SELECT * FROM users WHERE username = '{user3.username}'
                         """)
        user_cp = pen.fetchone()
        self.assertEqual(pen.rowcount, 1)
        user_attr_list = [attr for attr in user_cp]
        self.assertIn(user3.id, user_attr_list)
        self.assertIn(user3.name, user_attr_list)
        self.assertIn(user3.username, user_attr_list)
        self.assertIn(user3.email, user_attr_list)
        self.assertIn(user3.sex, user_attr_list)
        self.assertIn(user3.dob, user_attr_list)
        self.assertIn(user3.bio, user_attr_list)
        
        