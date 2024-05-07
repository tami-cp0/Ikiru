"""
Module to define socket for upload.js
"""
# from web_app.app import socket
from flask_socketio import send
from web_app.socketio import socket


@socket.on('upload', namespace="home")
def upload():
    pass