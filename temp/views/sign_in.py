#!/usr/bin/python3
from email import message
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError, Email
from models.user import User
from models import storage
from temp.app import bcrypt
from temp.views import app_views
from datetime import timedelta




class SignInForm(FlaskForm):
    """
    Class to sign in users
    """
    email = StringField(
        validators=[
            InputRequired(),
            Email(message="Invalid e-mail address")
        ],
        render_kw={
                    'id': 'email', 'class': 'form-inputs',
                    'placeholder': 'doe324@ikiru.tech or john12'
                   },
        label='Email or Username'
    )

    password = PasswordField(
        validators=[InputRequired(), Length(min=8)],
        render_kw={
                    'id': 'password', 'class': 'form-inputs',
                    'placeholder': '#123john%'
                   },
        label='Password'
    )

#  <div class="sign-in_options">
#                   <label for="keep_me_logged_in" id="keep_me"
#                     ><input
#                       type="checkbox"
#                       name="keep_me"
#                       value="keep_me"
#                       class="input_checkbox"
#                       id="keep_me_logged_in"
#                     >Keep me logged in</label
#                   >
#                   <a href="">Forgot password?</a>
#                 </div>
    keep_me = BooleanField(
        label="Keep me logged in",
        render_kw={
                    'class': 'input_checkbox', 'value': 'keep_me',
                    'id': 'keep_me_logged_in', 
                   }
    )
    
    submit = SubmitField(
        label="Sign in",
        render_kw={'class': 'signin_button', 'id': 'submit'}
    )


@app_views.route("/sign_in", methods=["GET", "POST"], strict_slashes=False)
def sign_in():
    form = SignInForm()
    
    if request.method == "POST":
        user = storage.get(User, email=form.email.data, username=form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):  
                if form.keep_me.data == True:
                    login_user(user, remember=True, duration=timedelta(minutes=2))
                else:
                    login_user(user)
                return redirect(url_for('app_views.home'))

        flash("Wrong email, username or password")
    return render_template('sign_in.html', form=form)



