#!/usr/bin/python3
"""
Home view
"""
from flask import Flask, render_template
from temp.views import app_views
from flask_login import current_user, login_required


@app_views.route("/home", strict_slashes=False)
@login_required
def home():
    return render_template("base.html", user=current_user.to_dict())
