#!/usr/bin/python3
"""
Settings view
"""
from flask import render_template
from web_app.views import app_views
from flask_login import current_user, login_required


@app_views.route("/<username>/settings", strict_slashes=False)
@login_required
def settings(username):
    return render_template("settings.html", user=current_user.to_dict())
