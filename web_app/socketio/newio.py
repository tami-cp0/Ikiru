from flask import request
from flask_login import current_user
from flask_socketio import emit, Namespace


online = {}
class InboxMessage(Namespace):
    def on_connect(self):
        if current_user.is_authenticated:
            online[current_user.username] = request.sid
            print(f"{current_user.username} connneted with id {request.sid}")


    def on_disconnect(self):
        if current_user.is_authenticated and current_user.username in online:
            del online[current_user.username]
            print(f"{current_user.username} disconnneted with id {request.sid}")
    
  
  
    def on_message(self, data):
        #save the post to db before emit
        #if data["receiver_username"] in online:
        print(data)
            #room = online[data["receiver_username"]]
        namespace = "/{}".format(data.get("room"))
        print(namespace)
            #emit("receiver_message", data, namespace="/msg")
            #send instant post to all user on home page
            #namespace = f"/{data['receiver_username']}"
        emit("receive_message", data["content"], namespace="/private", broadcast=True)
