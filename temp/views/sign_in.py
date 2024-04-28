#!/usr/bin/python3
from flask import Flask, jsonify, render_template, url_for, redirect, flash
from flask_login import login_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Email
from models.user import User
from models import storage
from temp.app import bcrypt, login_manager
from temp.views import app_views



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

    submit = SubmitField(
        label="Sign in",
        render_kw={'class': 'signin_button', 'id': 'submit'}
    )


@app_views.route("/sign_in", methods=["GET", "POST"], strict_slashes=False)
def sign_in():
    form = SignInForm()
    
    user = storage.get(User, email=form.email.data, username=form.email.data)
    print(user)
    if user:
        if bcrypt.check_password_hash(user.password, form.password.data):    
            login_user(user)
            print(current_user)
            return redirect(url_for('app_views.home'))
        else:
            flash("Wrong Email or Password")
    else:
        flash("Wrong Email or Password")

    return render_template('sign_in.html', form=form)
