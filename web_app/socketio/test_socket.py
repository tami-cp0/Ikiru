"""
Module to define socket for upload.js
"""
from web_app.app import socket
from flask_socketio import send

@socket.on('upload', namespace="home")
def upload():
    pass



# <a href="{{ url_for('msg', username=user.username) }}">inbox</a>
# @app.route("/msg/<username>", strict_slashes=False)
# @login_required
# def msg(username):
#     return render_template("msg.html", user=current_user.to_dict(), username=username)


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
