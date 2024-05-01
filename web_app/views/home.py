#!/usr/bin/python3
"""
Home view
"""
from pipes import quote
from flask import Flask, render_template
from web_app.views import app_views
from flask_login import current_user, login_required
from models import storage
from models.user import User
from models.post import Post
import random
import requests
from datetime import timedelta, datetime

last_request = None
quotes = None

@app_views.route("/home", strict_slashes=False)
@login_required
def home():
    user = current_user.to_dict()

    posts = storage.all(Post).values()
    posts_data = []
    for post in posts:
        if post.user_id == current_user.id:
            continue
        data = post.to_dict()
        user = storage.get(User, id=post.user_id)
        data["name"] = user.name
        data["username"] = user.username
        data["comments"] = len(post.comments)
        posts_data.append(data)

    posts = random.choice(posts_data)
    
    
    global last_request
    global quotes

    if last_request is None or datetime.now() - last_request > timedelta(minutes=6) or quotes is None:
        url = "https://zenquotes.io/api/quotes"
        response = requests.get(url, allow_redirects=False).json()
        quotes = response[:3]
        last_request = datetime.now() 

    return render_template("home.html", user=current_user.to_dict(), posts=posts_data, quotes=quotes)

@app_views.route("/base", strict_slashes=False)
@login_required
def base():
    return render_template("base.html", user=current_user.to_dict())
