#!/usr/bin/python3
"""
Home view
"""
from flask import Flask, render_template
from temp.views import app_views
from flask_login import current_user, login_required
from temp.app import login_manager


@app_views.route("/home", strict_slashes=False)
@login_required
def home():
    print(current_user)
    return render_template("base.html", user=current_user.to_dict())