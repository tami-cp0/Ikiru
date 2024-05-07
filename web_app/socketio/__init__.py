from flask_socketio import SocketIO
socket = SocketIO(cors_allowed_origins="*")
from web_app.socketio.newio import InboxMessage

socket.on_namespace(InboxMessage("/private"))