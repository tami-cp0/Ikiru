from flask_socketio import emit, send
from flask import request
from zmq import Message
from temp.app import socket

# @socket.on("connect")
# def handle_connect():
#     """print 'connect' every time client connect through socketIO"""
#     print("connect")
  
# @socket.on("sent_message")
# def handle_sent_message(json_message):
#     """direct the sent message to the reveciver"""
#    # namespace = "/msg"+ json_message["receiver"] + "/" + request.sid
#     print("\n\n___________________________________________\n\n")
#     print(json_message)
    
#     print("\n\n________________________________________\n\n")
#     emit("received_msg", json_message, namespace="/msg")


