#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import json
import re
from models.user import User
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response


@apis.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrives all users
    """
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)


@apis.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Retrives a single user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@apis.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """
    Creates a user
    """
    try:
        data = request.get_json()
    except json.JSONDecodeError as e:
        print(f"Invalid JSON\nError: {e}")

    user = User(**data)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)
