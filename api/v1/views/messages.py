#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Conversations """
from models.user import User
from models.conversation import Conversation
from models.message import Message
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response


# indirect routes to conversations
@apis.route('/users/<user_id>/conversations/<conversation_id>/messages', methods=['GET'], strict_slashes=False)
def get_user_conversation_messages(user_id, conversation_id):
    """
    Retreives messages from a specific conversation of a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversation = storage.get(Conversation, conversation_id)
    if not(conversation or conversation not in user.conversations):
        abort(404, description="Conversation not found")
        
    messages = [message.to_dict() for message in conversation.messages]

    return jsonify(messages)


@apis.route('/<sender_id>/<receiver_id>/conversations/<conversation_id>/messages', methods=['POST'], strict_slashes=False)
def create_user_conversation_message(sender_id, receiver_id, conversation_id=None):
    """
    creates a conversationif its the first time
    Sends a message
    """
    sender_id = storage.get(User, sender_id)
    if not sender_id:
        abort(404, description="User not found")
        
    receiver_id = storage.get(User, receiver_id)
    if not receiver_id:
        abort(404, description="User not found")
        
    conversation = storage.get(Conversation, conversation_id)
    if not conversation:
        converse = Conversation(sender_id=sender_id, receiver_id=receiver_id)
        converse.save()

        # check if a convo between those two users already
        # exists, maybe leaving out conversation_id was a mistake
        conversations = storage.all(Conversation)
        for convo in conversations:
            if convo.sender_id == sender_id and convo.receiver_id == receiver_id:
                conversation = convo
                storage.delete(converse)
                storage.save()
                break
            else:
                conversation = converse
        
    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")
        
    data["conversation_id"] = conversation.id
    message = Message(**data)
    message.save()

    return make_response(jsonify(message.to_dict()), 201)


@apis.route('/users/<user_id>/conversations/<conversation_id>/messages/<message_id>', methods=['DELETE'], strict_slashes=False)
def delete_user_conversation_message(user_id, conversation_id, message_id):
    """
    Retreives messages from a specific conversation of a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversation = storage.get(Conversation, conversation_id)
    if not(conversation or conversation not in user.conversations):
        abort(404, description="Conversation not found")
    
    message = storage.get(Message, message_id)
    if not (message or message not in conversation.messages):
        abort(404, description="Message not found")
        
    storage.delete(message)
    storage.save()

    return make_response('', 204)


@apis.route('/users/<user_id>/conversations/<conversation_id>/messages/<message_id>', methods=['PUT'], strict_slashes=False)
def update_user_conversation_message(user_id, conversation_id, message_id):
    """
    Retreives messages from a specific conversation of a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversation = storage.get(Conversation, conversation_id)
    if not(conversation or conversation not in user.conversations):
        abort(404, description="Conversation not found")
    
    message = storage.get(Message, message_id)
    if not (message or message not in conversation.messages):
        abort(404, description="Message not found")
        
    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    ignore = ['id', 'created_at', 'updated_at',
              'is_reported', 'user_id', 'conversation_id']

    for key, value in data.items():
        if key not in ignore:
            setattr(message, key, value)
    message.save()
    return jsonify(message.to_dict())

