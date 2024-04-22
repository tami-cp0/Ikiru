#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Posts """
from models.user import User
from models.post import Post
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response


# direct routes with posts
@apis.route('/posts', methods=['GET'], strict_slashes=False)
def get_posts():
    """
    Retreives all posts
    """
    posts = [post.to_dict() for post in storage.all(Post).values()]
    return jsonify(posts)


@apis.route('/posts/<post_id>', methods=['GET'], strict_slashes=False)
def get_post(post_id):
    """
    Retreives a single post
    """
    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post does not exist")

    return jsonify(post.to_dict())


@apis.route('/posts/<post_id>', methods=['DELETE'], strict_slashes=False)
def delete_post(post_id):
    """
    Deletes a post
    """
    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post does not exist")

    storage.delete(post)
    storage.save()

    return make_response('', 204)


# indirect routes with post
@apis.route('/users/<user_id>/posts', methods=['GET'], strict_slashes=False)
def get_user_posts(user_id):
    """
    Retreives all the posts of a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User does not exist")

    posts = [post.to_dict() for post in user.posts]
    return jsonify(posts)


@apis.route('/users/<user_id>/posts', methods=['POST'], strict_slashes=False)
def create_post(user_id):
    """
    creating a post under a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User does not exist")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    data["user_id"] = user_id
    post = Post(**data)
    post.save()

    return make_response(jsonify(post.to_dict()), 201)


@apis.route('/users/<user_id>/posts/<post_id>', methods=['GET'],
            strict_slashes=False)
def get_user_post(user_id, post_id):
    """
    Retreives one post from a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User does not exist")

    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post does not exist")

    return jsonify(post.to_dict())


@apis.route('/users/<user_id>/posts/<post_id>', methods=['DELETE'],
            strict_slashes=False)
def delete_user_post(user_id, post_id):
    """
    Deletes one post from a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User does not exist")

    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post does not exist")

    storage.delete(post)
    storage.save()

    return make_response('', 204)
