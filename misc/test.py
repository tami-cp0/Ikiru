#!/usr/bin/python3

# import bcrypt
# from models import storage
# from models import conversation
# from models.conversation import Conversation
# from models.user import User
# from models.message import Message
# from models.post import Post
# from datetime import datetime, date
# from flask_bcrypt import Bcrypt




# user = storage.get(User, id="efd2e873-086e-4f7e-95f5-ffabc5a83e23")

# conversations = user.received_conversations
# print([conversation.to_dict() for conversation in conversations])





import random
from urllib import response
import requests
from datetime import timedelta, datetime

last_request = None
quotes = None

def home():
    global last_request
    global quotes
    
    if last_request is None or datetime.now() - last_request > timedelta(hours=6):
        url = "https://zenquotes.io/api/quotes"
        response = requests.get(url, allow_redirects=False).json()
        quotes = response[:3]
        last_request = datetime.now()
    else:
        quotes = quotes

    print(quotes)


home()

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