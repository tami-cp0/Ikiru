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
    global last_request
    global quotes

    if last_request is None or datetime.now() - last_request > timedelta(hours=6) or quotes is None:
        url = "https://zenquotes.io/api/quotes"
        response = requests.get(url, allow_redirects=False).json()
        quotes = response[:3]
        last_request = datetime.now() 

    return render_template("home.html", user=current_user.to_dict(), quotes=quotes)

@app_views.route("/base", strict_slashes=False)
@login_required
def base():
    return render_template("base.html", user=current_user.to_dict())
