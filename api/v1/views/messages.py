#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Messages """
from datetime import datetime
from models.user import User
from models.conversation import Conversation
from models.message import Message
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response
from flasgger import swag_from


# indirect routes to conversations
@apis.route(
    '/users/<user_id>/conversations/<conversation_id>/messages',
    methods=['GET'], strict_slashes=False
)
@swag_from('documentation/message/all_messages.yml')
def all_messages(user_id, conversation_id):
    """
    Retrieve all messages from a specific conversation under a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversations = user.sent_conversations + user.received_conversations

    conversation = storage.get(Conversation, conversation_id)
    if not (conversation or conversation in conversations):
        abort(404, description="Conversation not found")

    user1 = storage.get(User, conversation.sender_id)
    user2 = storage.get(User, conversation.receiver_id)

    messages = [message.to_dict() for message in conversation.messages]
    for message in messages:
        if message["user_id"] == user1.id:
            message["name"] = user1.name
            message["username"] = user1.username
        else:
            message["name"] = user2.name
            message["username"] = user2.username

    return jsonify(messages)


# last api for huclark: get one message from the convo


@apis.route(
    '/<sender_id>/<receiver_id>/conversations/<conversation_id>',
    methods=['POST'], strict_slashes=False
)
@swag_from('documentation/message/post_message.yml')
def post_message(sender_id, receiver_id, conversation_id=None):
    """
    Create a new message in an existing conversation
    or
    create a new conversation then the message.
    """
    sender = storage.get(User, sender_id)
    if not sender:
        abort(404, description="User not found")

    receiver = storage.get(User, receiver_id)
    if not receiver:
        abort(404, description="User not found")

    conversation = storage.get(Conversation, conversation_id)
    if not conversation:
        # check if a convo between those two users already
        # exists, maybe leaving out conversation_id was a mistake
        conversations = storage.all(Conversation).values()
        for convo in conversations:
            if (convo.sender_id == sender_id and
               convo.receiver_id == receiver_id):
                conversation = convo
                exists = True
                break
            else:
                exists = False

        if exists is False:
            conversation = Conversation(sender_id=sender_id,
                                        receiver_id=receiver_id)
            conversation.save()

    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    data["user_id"] = sender_id
    data["conversation_id"] = conversation.id
    message = Message(**data)
    message.save()

    return make_response(jsonify(message.to_dict()), 201)


@apis.route(
    '/users/<user_id>/conversations/<conversation_id>/messages/<message_id>',
    methods=['DELETE'], strict_slashes=False
)
@swag_from('documentation/message/delete_message.yml')
def delete_message(user_id, conversation_id, message_id):
    """
    Delete a message
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversations = user.sent_conversations + user.received_conversations

    conversation = storage.get(Conversation, conversation_id)
    if not (conversation or conversation in conversations):
        abort(404, description="Conversation not found")

    message = storage.get(Message, message_id)
    if not (message or message in conversation.messages):
        abort(404, description="Message not found")

    storage.delete(message)
    storage.save()

    return make_response('', 204)


@apis.route(
    '/users/<user_id>/conversations/<conversation_id>/messages/<message_id>',
    methods=['PUT'], strict_slashes=False
)
@swag_from('documentation/message/update_message.yml')
def update_message(user_id, conversation_id, message_id):
    """
    Update a message
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversations = user.sent_conversations + user.received_conversations

    conversation = storage.get(Conversation, conversation_id)
    if not (conversation or conversation in conversations):
        abort(404, description="Conversation not found")

    message = storage.get(Message, message_id)
    if not (message or message in conversation.messages):
        abort(404, description="Message not found")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON")

    now = datetime.now()
    diff = now - message.created_at
    diff_in_minutes = divmod(diff.total_seconds(), 60)[0]

    if diff_in_minutes > 5.0:
        abort(400, description="too much time has passed")

    for key, value in data.items():
        if key == "content":
            setattr(message, key, value)
    message.save()
    return jsonify(message.to_dict())
