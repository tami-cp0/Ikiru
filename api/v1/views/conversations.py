#!/usr/bin/python3
""" Endpoints that handle all default RestFul API actions for Conversations """
from email import message
from models.user import User
from models.conversation import Conversation
from models import storage
from api.v1.views import apis
from flask import jsonify, abort, request, make_response
from flasgger import swag_from


# indirect routes to conversations
@apis.route(
    '/users/<user_id>/conversations',
    methods=['GET'], strict_slashes=False
)
@swag_from('documentation/conversation/all_conversations.yml')
def all_conversations(user_id):
    """
    Retrieve all conversations of a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversations = user.sent_conversations + user.received_conversations
    conversations_data = []

    for conversation in conversations:
        data = conversation.to_dict()
        data["participants"] = [
            {
                "name": conversation.sender.name,
                "sender_id": conversation.sender.id,
                "username": conversation.sender.username,
                "messages": len(
                    [message for message in conversation.messages
                     if message.user_id == conversation.sender.id]
                )
            },
            {
                "name": conversation.receiver.name,
                "receiver_id": conversation.receiver.id,
                "username": conversation.receiver.username,
                "messages": len(
                    [message for message in conversation.messages
                     if message.user_id == conversation.receiver.id]
                )
            }]
        data["messages"] = len(conversation.messages)
        del data["sender_id"]
        del data["receiver_id"]
        conversations_data.append(data)

    if conversations_data:
        conversations_data.sort(key=lambda x: x["created_at"])
    return jsonify(conversations_data)


@apis.route(
    '/users/<user_id>/conversations/<conversation_id>',
    methods=['GET'], strict_slashes=False
)
@swag_from('documentation/conversation/get_conversation.yml')
def get_conversation(user_id, conversation_id):
    """
    Retrieve a specific conversation of a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversations = user.sent_conversations + user.received_conversations

    conversation = storage.get(Conversation, conversation_id)
    if not (conversation or conversation in conversations):
        abort(404, description="Conversation not found")

    data = conversation.to_dict()
    data["participants"] = [
            {
                "name": conversation.sender.name,
                "sender_id": conversation.sender.id,
                "username": conversation.sender.username,
                "messages": len(
                    [message for message in conversation.messages
                     if message.user_id == conversation.sender.id]
                )
            },
            {
                "name": conversation.receiver.name,
                "receiver_id": conversation.receiver.id,
                "username": conversation.receiver.username,
                "messages": len(
                    [message for message in conversation.messages
                     if message.user_id == conversation.receiver.id]
                )
            }]
    data["messages"] = len(conversation.messages)
    del data["sender_id"]
    del data["receiver_id"]

    return jsonify(data)


@apis.route(
    '/users/<user_id>/conversations/<conversation_id>',
    methods=['DELETE'], strict_slashes=False
)
@swag_from('documentation/conversation/delete_conversation.yml')
def delete_conversation(user_id, conversation_id):
    """
    Delete a specific conversation of a specific user.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")

    conversations = user.sent_conversations + user.received_conversations

    conversation = storage.get(Conversation, conversation_id)
    if not (conversation or conversation in conversations):
        abort(404, description="Conversation not found")

    storage.delete(conversation)
    storage.save()

    return make_response('', 204)


# missing documentation
@apis.route(
    '/users/<user_id>/conversations/requests',
    methods=['GET'], strict_slashes=False
)
def requests(user_id):
    """
    Retrieve all conversations that a user hasnt sent a single message there
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="User not found")


    conversations_data = []

    conversations = user.received_conversations
    for conversation in conversations:
        sender = storage.get(User, id=conversation.sender.id)
        
        if len([message for message in conversation.messages if message.user_id == user_id]) == 0:
            data = {'convo_id': conversation.id, 'created_at': conversation.created_at,
                    'sender': sender.username, 'sender_id': sender.id}
            conversations_data.append(data)

    conversations_data.sort(key=lambda x: x["created_at"])

    return jsonify(conversations_data)
