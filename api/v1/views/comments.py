#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Comments """
from models.user import User
from models.post import Post
from models.comment import Comment
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response


# indirect routes with comments
@apis.route('/users/<user_id>/comments', methods=['GET'], strict_slashes=False)
def get_user_comments(user_id):
    """
    Retreives all comments from a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User does not exist")

    comments = [comment.to_dict() for comment in user.comment]
    return jsonify(comments)

