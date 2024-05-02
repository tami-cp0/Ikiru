#!/usr/bin/python3
import secrets
from flask import Flask, redirect, render_template, url_for, request
from web_app.views import app_views
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from models.user import User
from models import storage
from web_app.socketio.upload_socket import socket

app = Flask(__name__)
secret = "1b80974004ebbd9de8c0d22bb4906475b1"
app.config["SECRET_KEY"] = secret
app.config["SESSION_COOKIE_SECURE"] = True
app.config["REMEMBER_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True

login_manager = LoginManager()
login_manager.login_view = "app_views.sign_in"
login_manager.login_message = "Please Sign in to view this page."


@login_manager.user_loader
def load_user(id):
    return storage.get(User, id=id)


login_manager.init_app(app)
bcrypt = Bcrypt(app)
socket.init_app(app)


@app.route('/')
@login_required
def root():
    return redirect(url_for("app_views.home"))


@app.route('/alx_sign_in', strict_slashes=False)
def alx_sign_in():
    admin = storage.get(User, username="alx")
    if not admin:
        admin = User(name="ALX", username="alx",
                     email="alx@ikiru.com", password="password")
        admin.save()

    login_user(admin)
    return redirect(url_for('app_views.home'))


@app.route('/log_out', strict_slashes=False)
@login_required
def log_out():
    logout_user()
    return redirect(url_for('app_views.sign_in'))


# <a href="{{ url_for('msg', username=user.username) }}">inbox</a>
@app.route("/msg/<username>", strict_slashes=False)
@login_required
def msg(username):
     return render_template("msg.html", user=current_user.to_dict(), username=username)


# @socket.on('message')
# def handle_message(message):
#     print("Recieved message: " + message)
#     if message != "User connected!":
#         send(message, broadcast=True, include_self=False)


# @socket.on('message')
# def on_join(data):
#     print("Recieved message: " + data['content'])
#     if data['content'] != "User connected!":
#         print(rooms())
#         room = data['room']
#         if room not in rooms():
#             join_room(room)
#         send(data['content'], to=room, broadcast=True)
        
    # io.join()
    # io.connect()
    
# @socket.on('join_room')
# def join_room(data):
#     room = data
#     print(f" room: {room}")
#     print(rooms())
    
    # if room not in rooms():
    #     join_room(room)
    
    
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


if __name__ == "__main__":
    app.register_blueprint(app_views)
    socket.run(app, host="0.0.0.0", port=5001,
               debug=True, use_reloader=True, log_output=True)
    # app.run(host="0.0.0.0", port=5001, debug=True)
