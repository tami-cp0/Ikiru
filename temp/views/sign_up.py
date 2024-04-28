#!/usr/bin/python3
"""
Sign Up view
"""
from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Regexp, Email
from models.user import User
from temp.app import bcrypt
from models import storage
from temp.views import app_views


class SignUpForm(FlaskForm):
    """
    Class to register users
    """
    USERNAME_REGEX = r'^[a-zA-Z0-9_]+$'

    name = StringField(
        validators=[InputRequired(), Length(min=6)],
        render_kw={
                    'placeholder': 'John Doe', 'id': 'name',
                    'class': 'form-inputs'
                },
        label="Name"
    )

    username = StringField(
        validators=[InputRequired(), Length(min=6),
                    Regexp(
                            USERNAME_REGEX,
                            message="Username can only \
                                     contain letters, \
                                     numbers, and underscores."
                          )
                    ],
        render_kw={
                    'id': 'username', 'class': 'form-inputs',
                    'placeholder': 'john123'
                   },
        label='Username'
    )

    email = StringField(
        validators=[
            InputRequired(),
            Email(message="Invalid e-mail address")
        ],
        render_kw={
                    'id': 'email', 'class': 'form-inputs',
                    'placeholder': 'doe324@ikiru.tech'
                   },
        label='Email'
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
        label="Sign up",
        render_kw={'class': 'signup_button', 'id': 'submit'}
    )
    
    
    def validate_email(self, email):
        """checks if the same email is already used"""
        existing_user = storage.get(User, email=email.data)
        
        if existing_user:
            raise ValidationError("This email already exists")
        
    
    def validate_username(self, username):
        """checks if the same username is already used"""
        existing_user = storage.get(User, username=username.data)
        
        if existing_user:
            raise ValidationError("This username already exists")
     
        
@app_views.route("/sign_up", methods=["GET", "POST"], strict_slashes=False)
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(
            name=form.name.data, email=form.email.data,
            username=form.username.data, password=password_hash
        )
        user.save()
        
        return redirect(url_for('app_views.sign_in'))

    return render_template('sign_up.html', form=form)
