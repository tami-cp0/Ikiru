#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Comments """
from models.user import User
from models.post import Post
from models.comment import Comment
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response


# no direct routes to comment(s)
# indirect routes to comments:
@apis.route('/users/<user_id>/comments', methods=['GET'], strict_slashes=False)
def get_user_comments(user_id):
    """
    Retreives all comments from a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    comments = [comment.to_dict() for comment in user.comments]
    return jsonify(comments)


@apis.route('/users/<user_id>/comments/<comment_id>', methods=['GET'], strict_slashes=False)
def get_user_comment(user_id, comment_id):
    """
    Retreives one comment from a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    comment = storage.get(Comment, comment_id)
    if not (comment or comment in user.comments):
        abort(404, description="Comment not found")

    return jsonify(comment.to_dict())


@apis.route('/users/<user_id>/comments/<comment_id>', methods=['DELETE'], strict_slashes=False)
def delete_user_comment(user_id, comment_id):
    """
    Deletes a comment from a specific user
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
def get_post_comments(post_id):
    """
    Retreives all comments from a specific post
    """
    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post not found")

    comments = [comment.to_dict() for comment in post.comments]

    return jsonify(comments)


@apis.route('/posts/<post_id>/comments/<comment_id>', methods=['GET'], strict_slashes=False)
def get_post_comment(post_id, comment_id):
    """
    Retreives one comments from a specific post
    """
    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post not found")

    comment = storage.get(Comment, comment_id)
    if not (comment or comment in post.comments):
        abort(404, description="Comment not found")

    return jsonify(comment.to_dict())



@apis.route('/users/<user_id>/posts/<post_id>/comments', methods=['POST'], strict_slashes=False)
def create_post_comment(user_id, post_id):
    """
    Retreives all comments from a specific post
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


@apis.route('/users/<user_id>/posts/<post_id>/comments', methods=['GET'], strict_slashes=False)
def get_post_comments_from_user(user_id, post_id):
    """
    Retreives all comments from a specific post
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    post = storage.get(Post, post_id)
    if not (post or post in user.posts):
        abort(404, description="Post not found")
        
    comments = [comment.to_dict() for comment in post.comments]
    
    return jsonify(comments)


@apis.route('/users/<user_id>/posts/<post_id>/comments/<comment_id>', methods=['DELETE'], strict_slashes=False)
def delete_post_comment(user_id, post_id, comment_id):
    """
    Retreives all comments from a specific post
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


@apis.route('/users/<user_id>/posts/<post_id>/comments/<comment_id>', methods=['GET'], strict_slashes=False)
def get_post_comment_from_user(user_id, post_id, comment_id):
    """
    Retreives all comments from a specific post
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
    
    return jsonify(comment.to_dict())