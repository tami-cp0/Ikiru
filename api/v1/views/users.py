#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Users """
from models.user import User
from models.post import Post
from models.comment import Comment
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response
from flasgger.utils import swag_from


# direct routes to users
@apis.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml', methods=['GET'])
def get_users():
    """
    Fetches all users with their related information.
    """
    users = storage.all(User).values()
    users_data = []
    for user in users:
        data = user.to_dict()
        data["posts"] = len(user.posts)
        data["comments"] = len(user.comments)
        conversations = user.sent_conversations + user.received_conversations
        data["conversations"] = len(conversations)
        users_data.append(data)

    return jsonify(users_data)


@apis.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(user_id):
    """
    Fetches a specific user's information.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")
    data = user.to_dict()
    data["posts"] = len(user.posts)
    data["comments"] = len(user.comments)
    conversations = user.sent_conversations + user.received_conversations
    data["conversations"] = len(conversations)

    return jsonify(data)


@apis.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """
    Creates a new user.
    """
    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    user = User(**data)
    user.save()
    data = user.to_dict()
    data["posts"] = len(user.posts)
    data["comments"] = len(user.comments)
    conversations = user.sent_conversations + user.received_conversations
    data["conversations"] = len(conversations)

    return make_response(jsonify(data), 201)


@apis.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """
    Updates a specific user's information.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at',
              'is_active', 'is_admin', 'is_reported']

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()
    data = user.to_dict()
    data["posts"] = len(user.posts)
    data["comments"] = len(user.comments)
    conversations = user.sent_conversations + user.received_conversations
    data["conversations"] = len(conversations)

    return make_response(jsonify(data), 200)


@apis.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")
    storage.delete(user)
    storage.save()

    return make_response('', 204)
