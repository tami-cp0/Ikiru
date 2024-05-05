#!/usr/bin/python3

import bcrypt
from models import storage
from models import conversation
from models.conversation import Conversation
from models.user import User
from models.message import Message
from models.post import Post
from datetime import datetime, date
from flask_bcrypt import Bcrypt




# user = storage.get(User, id="efd2e873-086e-4f7e-95f5-ffabc5a83e23")

# conversations = user.received_conversations
# print([conversation.to_dict() for conversation in conversations])
user = storage.get(User, id="2950d190-52ee-492c-bc4f-e062ec2b05a6")
total_posts = [post.to_dict() for post in user.posts]
total_posts.sort(key=lambda x: x["created_at"], reverse=True)
print(total_posts[0])





# import random
# from urllib import response
# import requests
# from datetime import timedelta, datetime





# response = requests.get("http://127.0.0.1:5000/api/v1/posts/9").json()
# print(response) 

# last_request = None
# quotes = None

# def home():
#     global last_request
#     global quotes
    
#     if last_request is None or datetime.now() - last_request > timedelta(hours=6):
#         url = "https://zenquotes.io/api/quotes"
#         response = requests.get(url, allow_redirects=False).json()
#         quotes = response[:3]
#         last_request = datetime.now()
#     else:
#         quotes = quotes

#     print(quotes)


# home()



    # user = current_user.to_dict()

    # posts = storage.all(Post).values()
    # posts_data = []
    # for post in posts:
    #     if post.user_id == current_user.id:
    #         continue
    #     data = post.to_dict()
    #     user = storage.get(User, id=post.user_id)
    #     data["name"] = user.name
    #     data["username"] = user.username
    #     data["comments"] = len(post.comments)
    #     posts_data.append(data)

    # posts = random.choice(posts_data)
# mydict = {"name": "Josh", "username": "ragoyam", "sex": "Male", "password": "as8asPju", "email": "joshal@gmail.com", "dob": "2010-04-17"}

# import secrets

# # Generate a secret key
# secret_key = secrets.token_hex(32)
# print(secret_key)


# user = storage.get(User, id="ba94b6e1-9c66-4802-9376-5e423c5a3806")
# user = User.query.filter_by(username="tami_cp0").first
# print(user)
# print(user.sent_conversations)
# conversation = storage.get(Conversation, 'f7707a8b-5bc9-436e-8b2e-50871f597853')
# data = {"content": "lolll", "user_id": user.id, "conversation_id": conversation.id}
# message = Message(**data)
# message.save()

# print(message.to_dict())
# print("participants: ")
# print(conversation.sender.name)
# print(conversation.receiver.name)
# print("sent:")
# print([convo.id for convo in user.sent_conversations])
# print("received")
# print([convo.id for convo in user.received_conversations])

# now = datetime.now()
# diff = now - user.created_at
# diff_in_minutes = divmod(diff.total_seconds(), 60)[0]
    
# if diff_in_minutes > 5:
#         print(f"{diff_in_minutes} minutes since creation")
#         print(f"        {user.created_at}")
#         print("        =========================")
#         print(f"        {now}")
# # abort(400, description="too much time has passed")

# if (cls or id) == None:
#         return None