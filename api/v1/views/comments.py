#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Comments """
from models.user import User
from models.post import Post
from models.comment import Comment
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response
from flasgger import swag_from


# no direct routes to comment(s)
# indirect routes to comments:
@apis.route('/users/<user_id>/comments', methods=['GET'], strict_slashes=False)
@swag_from('documentation/comment/all_user_comments.yml')
def all_user_comments(user_id):
    """
    Retrieve all comments made by a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    comments = [comment.to_dict() for comment in user.comments]
    for comment in comments:
        post = storage.get(Post, comment['post_id'])
        post_user = storage.get(User, post.user_id)

        comment["username"] = user.username
        comment["name"] = user.name
        comment["post_owner_username"] = post_user.username
        comment["post_owner_name"] = post_user.name

    return jsonify(comments)


@apis.route(
    '/users/<user_id>/comments/<comment_id>',
    methods=['GET'], strict_slashes=False
)
@swag_from('documentation/comment/get_user_comment.yml')
def get_user_comment(user_id, comment_id):
    """
    Retrieve a specific comment from a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    comment = storage.get(Comment, comment_id)
    if not (comment or comment in user.comments):
        abort(404, description="Comment not found")
    comment = comment.to_dict()
    post = storage.get(Post, comment['post_id'])
    post_user = storage.get(User, post.user_id)

    comment["username"] = user.username
    comment["name"] = user.name
    comment["post_owner_username"] = post_user.username
    comment["post_owner_name"] = post_user.name

    return jsonify(comment)


@apis.route(
    '/users/<user_id>/comments/<comment_id>',
    methods=['DELETE'], strict_slashes=False
)
@swag_from('documentation/comment/delete_comment.yml')
def delete_comment(user_id, comment_id):
    """
    Delete a specific comment from a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    comment = storage.get(Comment, comment_id)
    if not (comment or comment in user.comments):
        abort(404, description="Comment not found")

    storage.delete(comment)
    storage.save()

    return make_response('', 204)


@apis.route('/posts/<post_id>/comments', methods=['GET'], strict_slashes=False)
@swag_from('documentation/comment/all_post_comments.yml')
def all_post_comments(post_id):
    """
    Retrieve all comments from a specific post.
    """
    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post not found")

    post_user = storage.get(User, post.user_id)

    comments = [comment.to_dict() for comment in post.comments]
    for comment in comments:
        user = storage.get(User, comment["user_id"])

        comment["username"] = user.username
        comment["name"] = user.name
        comment["post_owner_username"] = post_user.username
        comment["post_owner_name"] = post_user.name

    return jsonify(comments)


@apis.route(
    '/posts/<post_id>/comments/<comment_id>',
    methods=['GET'], strict_slashes=False
)
@swag_from('documentation/comment/get_comment.yml')
def get_comment(post_id, comment_id):
    """
    Retrieve a specific comment from a specific post.
    """
    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post not found")

    post_user = storage.get(User, post.user_id)

    comment = storage.get(Comment, comment_id)
    if not (comment or comment in post.comments):
        abort(404, description="Comment not found")
    comment = comment.to_dict()
    user = storage.get(User, comment["user_id"])

    comment["username"] = user.username
    comment["name"] = user.name
    comment["post_owner_username"] = post_user.username
    comment["post_owner_name"] = post_user.name

    return jsonify(comment)


@apis.route(
    '/users/<user_id>/posts/<post_id>/comments',
    methods=['POST'], strict_slashes=False
)
@swag_from('documentation/comment/post_comment.yml')
def post_comment(user_id, post_id):
    """
    Create a new comment for a specific post by a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    post = storage.get(Post, post_id)
    if not (post or post in user.posts):
        abort(404, description="Post not found")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    data["user_id"] = user_id
    data["post_id"] = post_id
    comment = Comment(**data)
    comment.save()

    return make_response(jsonify(comment.to_dict()), 201)


@apis.route(
    '/users/<user_id>/posts/<post_id>/comments',
    methods=['GET'], strict_slashes=False
)
@swag_from('documentation/comment/all_user_post_comments.yml')
def all_user_post_comments(user_id, post_id):
    """
    Retrieve all comments under a specific user post
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    post = storage.get(Post, post_id)
    if not (post or post in user.posts):
        abort(404, description="Post not found")

    comments = [comment.to_dict() for comment in post.comments]
    for comment in comments:
        comment_user = storage.get(User, comment["user_id"])
        comment["username"] = comment_user.username
        comment["name"] = comment_user.name
        comment["post_owner_username"] = user.username
        comment["post_owner_name"] = user.name

    return jsonify(comments)


@apis.route(
    '/users/<user_id>/posts/<post_id>/comments/<comment_id>',
    methods=['DELETE'], strict_slashes=False
)
@swag_from('documentation/comment/delete_comment_by_post_owner.yml')
def delete_comment_by_post_owner(user_id, post_id, comment_id):
    """
    Delete a specific comment by post owner
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    post = storage.get(Post, post_id)
    if not (post or post in user.posts):
        abort(404, description="Post not found")

    comment = storage.get(Comment, comment_id)
    if not (comment or comment in post.comments):
        abort(404, description="Comment not found")

    storage.delete(comment)
    storage.save()

    return make_response('', 204)


@apis.route(
    '/users/<user_id>/posts/<post_id>/comments/<comment_id>',
    methods=['GET'], strict_slashes=False
)
@swag_from('documentation/comment/get_single_comment_under_user_post.yml')
def get_single_comment_under_user_post(user_id, post_id, comment_id):
    """
    Retrieve a specific comment under a user's post
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    post = storage.get(Post, post_id)
    if not (post or post in user.posts):
        abort(404, description="Post not found")

    comment = storage.get(Comment, comment_id)
    if not (comment or comment in post.comments):
        abort(404, description="Comment not found")
    comment = comment.to_dict()
    comment_user = storage.get(User, comment["user_id"])

    comment["username"] = comment_user.username
    comment["name"] = comment_user.name
    comment["post_owner_username"] = user.username
    comment["post_owner_name"] = user.name

    return jsonify(comment)
