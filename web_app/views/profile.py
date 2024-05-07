#!/usr/bin/python3
"""
Profile view
"""
from flask import render_template
from web_app.views import app_views
from flask_login import current_user, login_required
from models import storage
from models.user import User


@app_views.route("/<username>", strict_slashes=False)
@login_required
def profile(username):
    user = current_user.to_dict()
    print(f"u==========\n{username}: me; {user['username']}\n==========================")
    if username != user['username']:
        user2 = storage.get(User, username=username).to_dict()
        return render_template("profile-otheruser.html", user=user, user2=user2)
    
    return render_template("profile.html", user=user)
