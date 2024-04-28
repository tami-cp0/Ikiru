#!/usr/bin/python3
from flask import Flask, redirect, url_for
from temp.views import app_views
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, current_user
from models.user import User


app = Flask(__name__)
app.config["SECRET_KEY"] = "skajkn283728732"


bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.login_view = "app_views.sign_in"

@login_manager.user_loader
def load_user(id):
    from models import storage
    print("======================")
    print(id)
    print("======================")
    return storage.get(User, id=id)

login_manager.init_app(app)


@app.route('/')
@login_required
def root():
    return redirect(url_for("app_views.home"))

    
if __name__ == "__main__":
    app.register_blueprint(app_views)
    app.run(host="0.0.0.0", port=5001, debug=True)
