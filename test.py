#!/usr/bin/python3

from models.user import User
from models import storage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


