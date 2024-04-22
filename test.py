#!/usr/bin/python3

from models import storage
from models.conversation import Conversation
from models.user import User
from datetime import date

dat = "2000-04-02"
con = date.fromisoformat(dat)
print(con)