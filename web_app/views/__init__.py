#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from web_app.views.sign_up import *
from web_app.views.sign_in import *
from web_app.views.home import *
