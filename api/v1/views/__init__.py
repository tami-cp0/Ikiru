#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

# add  url_prefix='/api/v1' later.
apis = Blueprint('apis', __name__)

from api.v1.views.users import *
from api.v1.views.posts import *
from api.v1.views.comments import *
from api.v1.views.conversations import *
from api.v1.views.messages import *
