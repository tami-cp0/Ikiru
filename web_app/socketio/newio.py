from flask import request
from flask_login import current_user
from flask_socketio import emit
from web_app.app import socket


online = {}

@socket.on("connect")
def handele_online():
    if current_user.is_authenticated:
        online[current_user.username] = request.sid
        print(f"{current_user.username} connneted with id {request.sid}")


@socket.on("disconnect")
def handele_offline():
    if current_user.is_authenticated and current_user.username in online:
        del online[current_user.username]
        print(f"{current_user.username} disconnneted with id {request.sid}")


@socket.on("home_post")
def handle_post(data):
    #save the post to db before emit

    #send instant post to all user on home page
    emit("post", data, namespace="/home")


@socket.on("sent_message")
def handle_message(data):
    #save the post to db before emit
    if data["receiver_username"] in online:
        room = online[data["receiver_username"]]
        #namespace = f"/msg/{data['receiver_username']}"
        emit("receiver_message", data, namespace="/msg")
        #send instant post to all user on home page
        #namespace = f"/home/{data['receiver_username']}"
       # emit("receive_message", data, namespace=namespace, room=room)
