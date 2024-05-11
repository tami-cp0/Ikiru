#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Posts """
from models.user import User
from models.post import Post
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response
from flasgger.utils import swag_from

current_posts = []
total_posts = []

# direct routes to posts
@apis.route('/posts/<int:num>/<refreshed>/<id>', methods=['GET'], strict_slashes=False)
def get_num_posts(num, refreshed, id):
    """
    Retrieves a number of posts from the database
    and notes the posts that havent been requested yet.
    This route is used to populate the FEED of the website
    """
    global current_posts
    global total_posts

    # if the refreshed was received by the api, it should reset all post tracking
    if refreshed == "refreshed":
        total_posts = []
        current_posts = []
        
    post_num = len(total_posts)

    # get posts from the database
    posts = storage.all(Post).values()    
    
    # if posts is greater than the posts in the global variable
    # then it should fetch them and add them to the total
    # posts for tracking
    if len(posts) > post_num:
        total_posts = []
        for post in posts:
            if post.user_id == id:
                continue
            data = post.to_dict()
            user = storage.get(User, post.user_id)
            data["name"] = user.name
            data["username"] = user.username
            data["comments"] = len(post.comments)
            total_posts.append(data)
        
        total_posts.sort(key=lambda x: x["created_at"], reverse=True)
        new_posts = total_posts[post_num:]
        
        # current posts hold posts the user
        # has not seen yet
        current_posts += new_posts
        
    # if the requested post is greater than the current posts
    # it should return that and empty the list
    # else it should return the number of posts requested 
    # and delete them from the current_posts list
    if num > len(current_posts):
        posts_data = current_posts
        current_posts = []
    else:
        posts_data = current_posts[:num]
        del current_posts[:num]
    
    return jsonify(posts_data)



@apis.route('/posts', methods=['GET'], strict_slashes=False)
@swag_from('documentation/post/all_posts.yml', methods=['GET'])
def get_posts():
    """
    Retrieves all posts from the database.
    """
    posts = storage.all(Post).values()
    posts_data = []
    for post in posts:
        data = post.to_dict()
        user = storage.get(User, post.user_id)
        data["name"] = user.name
        data["username"] = user.username
        data["comments"] = len(post.comments)
        posts_data.append(data)

    return jsonify(posts_data)


@apis.route('/posts/<post_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/post/get_post.yml', methods=['GET'])
def get_post(post_id):
    """
    Retrieves a specific post by its ID.
    """
    post = storage.get(Post, post_id)
    if not post:
        abort(404, description="Post not found")
    data = post.to_dict()
    user = storage.get(User, post.user_id)
    data["username"] = user.username
    data["name"] = user.name
    data["comments"] = len(post.comments)

    return jsonify(data)


# indirect routes to post
@apis.route('/users/<user_id>/posts', methods=['GET'], strict_slashes=False)
@swag_from('documentation/post/all_user_posts.yml', methods=['GET'])
def get_user_posts(user_id):
    """
    Retrieves all posts created by a specific user. IN ORDER OF CREATION
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    posts = user.posts
    posts_data = []
    for post in posts:
        data = post.to_dict()
        user = storage.get(User, post.user_id)
        data["username"] = user.username
        data["name"] = user.name
        data["comments"] = len(post.comments)
        posts_data.append(data)

    posts_data.sort(key=lambda x: x["created_at"], reverse=True)
    return jsonify(posts_data)


@apis.route('/users/<user_id>/posts', methods=['POST'], strict_slashes=False)
@swag_from('documentation/post/create_post.yml', methods=['POST'])
def create_post(user_id):
    """
    Creates a new post for a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not fonud")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    data["user_id"] = user_id
    post = Post(**data)
    post.save()
    
    data = post.to_dict()
    data["username"] = user.username
    data["name"] = user.name
    data["comments"] = len(post.comments)

    return make_response(jsonify(data), 201)


@apis.route(
    '/users/<user_id>/posts/<post_id>',
    methods=['GET'], strict_slashes=False
)
@swag_from('documentation/post/get_user_post.yml', methods=['GET'])
def get_user_post(user_id, post_id):
    """
    Retrieves a specific post created by a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    post = storage.get(Post, post_id)
    if not (post or post in user.posts):
        abort(404, description="Post not found")
    data = post.to_dict()
    user = storage.get(User, post.user_id)
    data["username"] = user.username
    data["name"] = user.name
    data["comments"] = len(post.comments)

    return jsonify(data)


@apis.route(
    '/users/<user_id>/posts/<post_id>',
    methods=['DELETE'], strict_slashes=False
)
@swag_from('documentation/post/delete_post.yml', methods=['DELETE'])
def delete_post(user_id, post_id):
    """
    Deletes a specific post created by a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    post = storage.get(Post, post_id)
    if not (post or post in user.posts):
        abort(404, description="Post not found")

    storage.delete(post)
    storage.save()

    return make_response('', 204)
