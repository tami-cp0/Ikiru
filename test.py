#!/usr/bin/python3

from models import storage
from models.conversation import Conversation
from models.user import User
from models.post import Post
from datetime import date

mydict = {"name": "Josh", "username": "ragoyam", "sex": "Male", "password": "as8asPju", "email": "joshal@gmail.com", "dob": "2010-04-17"}

user = storage.get(User, "f66aa003-d2c7-4bf1-b538-251c26df0dbb")
print(user.posts)