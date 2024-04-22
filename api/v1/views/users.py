#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Users """
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
        abort(404, description="User does not exist")
    return jsonify(user.to_dict())


@apis.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """
    Creates a user
    """
    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    user = User(**data)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@apis.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """
    Updates a user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User does not exist")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at',
              'is_active', 'is_admin', 'is_reported']

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()
    return make_response(jsonify(user.to_dict()), 200)


@apis.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User does not exist")
    storage.delete(user)
    storage.save()

    return make_response('', 204)
