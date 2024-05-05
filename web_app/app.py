#!/usr/bin/python3
import secrets
from flask import Flask, redirect, render_template, url_for
from web_app.views import app_views
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from models.user import User
from models import storage
from flask_socketio import SocketIO

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
socket = SocketIO(cors_allowed_origins="*")
socket.init_app(app)


@app.route('/')
@login_required
def root():
    return redirect(url_for("app_views.home",
                            username=current_user.to_dict().username))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/alx_sign_in', strict_slashes=False)
def alx_sign_in():
    admin = storage.get(User, username="alx")
    if not admin:
        admin = User(name="ALX", username="alx",
                     email="alx@ikiru.com", password="password")
        admin.save()

    login_user(admin)
    return redirect(url_for('app_views.home',
                            username=current_user.to_dict().username))


@app.route('/log_out', strict_slashes=False)
@login_required
def log_out():
    logout_user()
    return redirect(url_for('app_views.sign_in'))


if __name__ == "__main__":
    app.register_blueprint(app_views)
    socket.run(app, host="0.0.0.0", port=5001,
               debug=True, use_reloader=True, log_output=True)
    # app.run(host="0.0.0.0", port=5001, debug=True)
