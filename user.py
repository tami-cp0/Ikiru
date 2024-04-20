from datetime import date
from models import storage
from models.user import User
user = User(username="ikiru1", sex="M", email="ikiru1@ikir.com", name="Ikiru", dob=date(2000, 4, 10), password="ikiru    ", bio="i live here")
user.save()
uid = user.id
user.delete()
storage.save()
print(storage.get(User, uid) == None)
