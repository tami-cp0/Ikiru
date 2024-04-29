from flask_socketio import emit
from flask import request
from temp.ikiruIO import socket

@socket.on("connect")
def handle_connect():
    """print 'connect' every time client connect through socketIO"""
    print("connect")
  
@socket.on("sent_message")
def handle_sent_message(json_message):
    """direct the sent message to the reveciver"""
    namespace = "/msg"+ json_message["receiver"] + "/" + request.sid
    emit("received_msg", json_message, namespace="/msg")
