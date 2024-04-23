#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Conversations """
from models.user import User
from models.conversation import Conversation
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response


# indirect routes to conversations
@apis.route('/users/<user_id>/conversations', methods=['GET'], strict_slashes=False)
def get_user_conversations(user_id):
    """
    Retreives all conversations of a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")
    sent_conversations = [conversation.to_dict() for conversation in user.sent_conversations]
    received_conversations = [conversation.to_dict() for conversation in user.received_conversations]
    conversations = sent_conversations + received_conversations
    return jsonify(conversations)


@apis.route('/users/<user_id>/conversations/<conversation_id>', methods=['GET'], strict_slashes=False)
def get_user_conversation(user_id, conversation_id):
    """
    Retreives a specific conversation of a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversation = storage.get(Conversation, conversation_id)
    if not(conversation or conversation not in user.conversations):
        abort(404, description="Conversation not found")
    
    return jsonify(conversation.to_dict())


@apis.route('/users/<user_id>/conversations/<conversation_id>', methods=['DELETE'], strict_slashes=False)
def delete_user_conversation(user_id, conversation_id):
    """
    deletes a specific conversation of a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversation = storage.get(Conversation, conversation_id)
    if not(conversation or conversation not in user.conversations):
        abort(404, description="Conversation not found")
    
    storage.delete(conversation)
    storage.save()

    return make_response('', 204)
