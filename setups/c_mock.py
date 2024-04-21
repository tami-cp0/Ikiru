#!/usr/bin/python3
"""
Generate mock data for database.

users - 5
post per user - 5
comment per user - 2
message per user - 5
10 unique conversations
"""
import json
from models import storage
from models.user import User
from models.post import Post
from models.comment import Comment
from models.message import Message


# path to files
files = ["setups/mock_data/user_mock.json", "setups/mock_data/post_mock.json", \
         "setups/mock_data/comment_mock.json", "setups/mock_data/message_mock.json"]

with open(files[0], "r") as user_file, open(files[1], "r") as post_file, \
     open(files[2], "r") as comment_file, open(files[3], "r") as message_file:
        users = json.load(user_file)
        posts = json.load(post_file)
        comments = json.load(comment_file)
        messages = json.load(message_file)
