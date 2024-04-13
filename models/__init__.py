#!/usr/bin/python3
"""Instantiates a DBStorage instance"""
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
