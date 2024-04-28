#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from temp.views.sign_up import *
from temp.views.sign_in import *
from temp.views.home import *

