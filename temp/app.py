#!/usr/bin/python3
from flask import Flask, redirect, url_for
from temp.views import app_views
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, login_user, logout_user
from models.user import User
from models import storage


app = Flask(__name__)
app.config["SECRET_KEY"] = "skajkn283728732"


bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.login_view = "app_views.sign_in"
login_manager.login_message = "Please Sign in to view this page."

@login_manager.user_loader
def load_user(id):
    return storage.get(User, id=id)

login_manager.init_app(app)


@app.route('/')
@login_required
def root():
    return redirect(url_for("app_views.home"))

@app.route('/alx_sign_in', strict_slashes=False)
def alx_sign_in():
    admin = storage.get(User, username="alx")
    if not admin:
        admin = User(name="ALX", username="alx", email="alx@ikiru.com", password="password")
        admin.save()
    
    login_user(admin)
    return redirect(url_for('app_views.home'))


@app.route('/log_out', strict_slashes=False)
@login_required
def log_out():
    logout_user()
    return redirect(url_for('app_views.sign_in'))

   
if __name__ == "__main__":
    app.register_blueprint(app_views)
    app.run(host="0.0.0.0", port=5001, debug=True)
