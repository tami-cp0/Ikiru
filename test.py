#!/usr/bin/python3

from models import storage
from models.conversation import Conversation
from models.user import User
from models.post import Post
from datetime import date

mydict = {"name": "Josh", "username": "ragoyam", "sex": "Male", "password": "as8asPju", "email": "joshal@gmail.com", "dob": "2010-04-17"}

user = storage.get(User, "dbad14da-c049-4008-ab5d-87bc0b698415")
posts = storage.get(Post, "f53d1a8d-a40d-4568-aa27-38647d648373")
print([convo.id for convo in user.sent_conversation])
print()
print([convo.id for convo in user.received_conversation])