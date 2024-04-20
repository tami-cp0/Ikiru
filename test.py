#!/usr/bin/python3

from datetime import date
from models.user import User
user = User(username="nkasanasikuru", sex="M", email="iasasa1@ikir.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru    ", bio="i live here")
print(str(user))
user.save()