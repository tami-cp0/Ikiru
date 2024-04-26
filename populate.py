#!/usr/bin/python3
"""
Generate mock data for database.

users list contains 10 (users MUST BE in multiples of 5)

OTHER LISTS MUST BE IN MULTIPLES OF 10
posts list contains 40
comments list contains 20
messages list contains 80

so if you want to add to these just copy and paste 
make sure its in multiples of 10
so like copy 10 or 1000 or whatever and paste
"""
import json
import os
import random
from datetime import date
from models import storage
from models.user import User
from models.post import Post
from models.comment import Comment
from models.message import Message
from models.conversation import Conversation
from fabric.api import local


dir = os.getcwd()

# ANSI escape code for blue text
BLUE = "\033[34m"
# ANSI escape code for resetting text color to default
RESET = "\033[0m"
# ANSI escape code for green text
GREEN = "\033[32m"
print(GREEN + "     --RESETTING DATABASE--" + RESET)

if not dir.endswith("Ikiru"):
    print(BLUE + "This script can only be run in the Ikiru directory" + RESET)
    exit(1)
local('cat setups/reset_db.sql | mysql -u ikiru_user --password="password"')
local('echo "quit" | ./console.py')
print(GREEN + "--DB reset complete--" + RESET)
users = [
    {
        "name": "Roseline",
        "username": "r0seline",
        "sex": "Female",
        "password": "nS5OAw7Ec",
        "email": "rbail0@themeforest.net",
        "dob": "2005-01-04"
    },
    {
        "name": "Vikky",
        "username": "vikky",
        "sex": "Female",
        "password": "jP5S$BJPju",
        "email": "vwatson1@noaa.gov",
        "dob": "2001-09-17"
    },
    {
        "name": "Gwynne",
        "username": "spider_w",
        "sex": "Female",
        "bio": "Duis mattis egestas metus. Aenean fermentum. Donec ut mauris eget massa tempor convallis.",
        "password": "lL8BB3S6s",
        "email": "gwaddilove2@spiegel.de",
        "dob": "2003-07-22"
    },
    {
        "name": "John",
        "username": "john12",
        "sex": "Male",
        "password": "oK01hCaOt!D5xHO",
        "email": "drundle3@abc.net.au",
        "dob": "2007-05-06"
    },
    {
        "name": "Sandor",
        "username": "sand0r",
        "sex": "Male",
        "password": "eM1P<l?55MAL",
        "email": "spolhill4@fastcompany.com",
        "dob": "1997-11-18"
    },
    {
        "name": "doe",
        "username": "unknown12",
        "sex": "Female",
        "password": "dfofddf",
        "email": "deo2332@gmail.com",
        "dob": "2000-01-06"
    },
    {
        "name": "Amaka",
        "username": "poundoyam",
        "sex": "Female",
        "password": "98asPju",
        "email": "amakareal@gmail.com",
        "dob": "2007-03-07"
    },
    {
        "name": "Esther",
        "username": "pinkprincess",
        "sex": "Female",
        "bio": "Duis mattis egestas metus. Aenean fermentum. Donec ut mauris eget massa tempor convallis.",
        "password": "eronetn4",
        "email": "pinky@gmail.com",
        "dob": "2003-09-22"
    },
    {
        "name": "Femi",
        "username": "viper001",
        "sex": "Male",
        "password": "tet!D5xHO",
        "email": "femi23@gmail.com",
        "dob": "2001-03-07"
    },
    {
        "name": "Bolu",
        "username": "purplepineapple",
        "sex": "Male",
        "password": "bolu?55MAL",
        "email": "bolu@gmail.com",
        "dob": "1999-01-08"
    }
]

posts = [
    {
        "content": "Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue."
    },
    {
        "content": "Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat."
    },
    {
        "content": "Suspendisse potenti.",
        "is_reported": False
    },
    {
        "content": "Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.",
        "is_anonymous": True
    },
    {
        "content": "Duis mattis egestas metus. Aenean fermentum. Donec ut mauris eget massa tempor convallis.",
        "is_anonymous": True
    },
    {
        "content": "Nulla justo.",
        "is_anonymous": True
    },
    {
        "content": "Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue."
    },
    {
        "content": "Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla."
    },
    {
        "content": "In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat. Nulla nisl. Nunc nisl."
    },
    {
        "content": "Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.",
        "is_anonymous": False
    },
    {
        "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.",
        "is_reported": True
    },
    {
        "content": "In congue.",
        "is_anonymous": True
    },
    {
        "content": "Vivamus vel nulla eget eros elementum pellentesque. Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla."
    },
    {
        "content": "In sagittis dui vel nisl. Duis ac nibh."
    },
    {
        "content": "Sed accumsan felis. Ut at dolor quis odio consequat varius.",
        "is_anonymous": True
    },
    {
        "content": "Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem. Sed sagittis.",
        "is_anonymous": True
    },
    {
        "content": "Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
        "is_reported": True
    },
    {
        "content": "Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.",
        "is_reported": True
    },
    {
        "content": "Aliquam sit amet diam in magna bibendum imperdiet.",
        "is_anonymous": True
    },
    {
        "content": "Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
        "is_anonymous": False
    },
    {
        "content": "Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue."
    },
    {
        "content": "Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat."
    },
    {
        "content": "Suspendisse potenti.",
        "is_reported": False
    },
    {
        "content": "Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.",
        "is_anonymous": True
    },
    {
        "content": "Duis mattis egestas metus. Aenean fermentum. Donec ut mauris eget massa tempor convallis.",
        "is_anonymous": True
    },
    {
        "content": "Nulla justo.",
        "is_anonymous": True
    },
    {
        "content": "Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue."
    },
    {
        "content": "Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla."
    },
    {
        "content": "In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat. Nulla nisl. Nunc nisl."
    },
    {
        "content": "Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.",
        "is_anonymous": False
    },
    {
        "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.",
        "is_reported": True
    },
    {
        "content": "In congue.",
        "is_anonymous": True
    },
    {
        "content": "Vivamus vel nulla eget eros elementum pellentesque. Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla."
    },
    {
        "content": "In sagittis dui vel nisl. Duis ac nibh."
    },
    {
        "content": "Sed accumsan felis. Ut at dolor quis odio consequat varius.",
        "is_anonymous": True
    },
    {
        "content": "Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem. Sed sagittis.",
        "is_anonymous": True
    },
    {
        "content": "Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
        "is_reported": True
    },
    {
        "content": "Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.",
        "is_reported": True
    },
    {
        "content": "Aliquam sit amet diam in magna bibendum imperdiet.",
        "is_anonymous": True
    },
    {
        "content": "Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
        "is_anonymous": False
    }
]

comments = [
    {
        "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus.",
        "is_reported": False
    },
    {
        "content": "Curabitur gravida nisi at nibh."
    },
    {
        "content": "Vivamus in felis eu sapien cursus vestibulum. Proin eu mi. Nulla ac enim."
    },
    {
        "content": "Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh."
    },
    {
        "content": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh."
    },
    {
        "content": "Etiam justo. Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna.",
        "is_reported": True
    },
    {
        "content": "Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem."
    },
    {
        "content": "Sed ante.",
        "is_reported": True,
        "is_anonymous": False
    },
    {
        "content": "Proin interdum mauris non ligula pellentesque ultrices."
    },
    {
        "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit."
    },
    {
        "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus.",
        "is_reported": False
    },
    {
        "content": "Curabitur gravida nisi at nibh."
    },
    {
        "content": "Vivamus in felis eu sapien cursus vestibulum. Proin eu mi. Nulla ac enim."
    },
    {
        "content": "Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh."
    },
    {
        "content": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh."
    },
    {
        "content": "Etiam justo. Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna.",
        "is_reported": True
    },
    {
        "content": "Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem."
    },
    {
        "content": "Sed ante.",
        "is_reported": True,
        "is_anonymous": False
    },
    {
        "content": "Proin interdum mauris non ligula pellentesque ultrices."
    },
    {
        "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit."
    },
]

messages = [
    {
        "content": "Morbi non quam nec dui luctus rutrum. Nulla tellus.",
        "is_reported": False
    },
    {
        "content": "Suspendisse potenti. Nullam porttitor lacus at turpis."
    },
    {
        "content": "Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem."
    },
    {
        "content": "Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus."
    },
    {
        "content": "Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc."
    },
    {
        "content": "Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum."
    },
    {
        "content": "Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo."
    },
    {
        "content": "Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna."
    },
    {
        "content": "Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa."
    },
    {
        "content": "Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi."
    },
    {
        "content": "Etiam pretium iaculis justo."
    },
    {
        "content": "Suspendisse ornare consequat lectus."
    },
    {
        "content": "Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla."
    },
    {
        "content": "Vivamus tortor. Duis mattis egestas metus."
    },
    {
        "content": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis."
    },
    {
        "content": "Nullam molestie nibh in lectus. Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus."
    },
    {
        "content": "Praesent lectus. Vestibulum quam sapien, varius ut, blandit non, interdum in, ante."
    },
    {
        "content": "Vivamus vestibulum sagittis sapien.",
        "is_reported": False
    },
    {
        "content": "Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc."
    },
    {
        "content": "Nulla mollis molestie lorem. Quisque ut erat."
    },
    {
        "content": "Morbi non quam nec dui luctus rutrum. Nulla tellus.",
        "is_reported": False
    },
    {
        "content": "Suspendisse potenti. Nullam porttitor lacus at turpis."
    },
    {
        "content": "Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem."
    },
    {
        "content": "Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus."
    },
    {
        "content": "Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc."
    },
    {
        "content": "Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum."
    },
    {
        "content": "Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo."
    },
    {
        "content": "Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna."
    },
    {
        "content": "Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa."
    },
    {
        "content": "Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi."
    },
    {
        "content": "Etiam pretium iaculis justo."
    },
    {
        "content": "Suspendisse ornare consequat lectus."
    },
    {
        "content": "Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla."
    },
    {
        "content": "Vivamus tortor. Duis mattis egestas metus."
    },
    {
        "content": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis."
    },
    {
        "content": "Nullam molestie nibh in lectus. Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus."
    },
    {
        "content": "Praesent lectus. Vestibulum quam sapien, varius ut, blandit non, interdum in, ante."
    },
    {
        "content": "Vivamus vestibulum sagittis sapien.",
        "is_reported": False
    },
    {
        "content": "Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc."
    },
    {
        "content": "Nulla mollis molestie lorem. Quisque ut erat."
    },
    {
        "content": "Morbi non quam nec dui luctus rutrum. Nulla tellus.",
        "is_reported": False
    },
    {
        "content": "Suspendisse potenti. Nullam porttitor lacus at turpis."
    },
    {
        "content": "Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem."
    },
    {
        "content": "Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus."
    },
    {
        "content": "Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc."
    },
    {
        "content": "Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum."
    },
    {
        "content": "Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo."
    },
    {
        "content": "Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna."
    },
    {
        "content": "Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa."
    },
    {
        "content": "Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi."
    },
    {
        "content": "Etiam pretium iaculis justo."
    },
    {
        "content": "Suspendisse ornare consequat lectus."
    },
    {
        "content": "Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla."
    },
    {
        "content": "Vivamus tortor. Duis mattis egestas metus."
    },
    {
        "content": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis."
    },
    {
        "content": "Nullam molestie nibh in lectus. Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus."
    },
    {
        "content": "Praesent lectus. Vestibulum quam sapien, varius ut, blandit non, interdum in, ante."
    },
    {
        "content": "Vivamus vestibulum sagittis sapien.",
        "is_reported": False
    },
    {
        "content": "Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc."
    },
    {
        "content": "Nulla mollis molestie lorem. Quisque ut erat."
    },
    {
        "content": "Morbi non quam nec dui luctus rutrum. Nulla tellus.",
        "is_reported": False
    },
    {
        "content": "Suspendisse potenti. Nullam porttitor lacus at turpis."
    },
    {
        "content": "Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem."
    },
    {
        "content": "Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus."
    },
    {
        "content": "Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc."
    },
    {
        "content": "Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum."
    },
    {
        "content": "Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo."
    },
    {
        "content": "Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna."
    },
    {
        "content": "Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa."
    },
    {
        "content": "Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi."
    },
    {
        "content": "Etiam pretium iaculis justo."
    },
    {
        "content": "Suspendisse ornare consequat lectus."
    },
    {
        "content": "Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla."
    },
    {
        "content": "Vivamus tortor. Duis mattis egestas metus."
    },
    {
        "content": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis."
    },
    {
        "content": "Nullam molestie nibh in lectus. Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus."
    },
    {
        "content": "Praesent lectus. Vestibulum quam sapien, varius ut, blandit non, interdum in, ante."
    },
    {
        "content": "Vivamus vestibulum sagittis sapien.",
        "is_reported": False
    },
    {
        "content": "Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc."
    },
    {
        "content": "Nulla mollis molestie lorem. Quisque ut erat."
    }
]

i = 0
for data in users:
    user = User(**data)
    user.save()
    for i in range(i, i + 4):
        posts[i]["user_id"] = user.id
        Post(**posts[i]).save()
    i += 1
    print(f"user {user.name} posted 5 times")
i = 0

user_instances = storage.all(User).values()
post_instances = storage.all(Post)
print(GREEN + "--all users have posted--" + RESET)
print("==========================================================")
     
j = 0
for user in user_instances:
    print(BLUE + f"{user.name}'s comments" + RESET)
    post_ids = [post.id for post in post_instances.values() if post.user_id != user.id]
    
    k = 0
    for k in range(k, k + 2):
        rand_id = random.choice(post_ids)
        i = 0

        comments[k]["post_id"] = rand_id
        comments[k]["user_id"] = user.id
        Comment(**comments[k]).save()
        post = storage.get(Post, rand_id)
        user_post = storage.get(User, post.user_id)
        print(f"    user {user.name} commented on {user_post.name}'s Post {post.id}")
    k += 1
    j += 1
    print("==========================================================")
print(GREEN + "--all users have commented--" + RESET)


def send_msg(conversation):
    # conversations = storage.all(Conversation).values()
    # end is maximum of 4 messages per convo
    end = 5
    j = 0
    # for conversation in conversations:
    count = 0
    first_restart = True # Flag to track the first restart
    sender = conversation.sender_id
    receiver = conversation.receiver.id
    message_range = range(1, end)
    rand_end = random.choice(message_range)
    for j in range(j, j + rand_end):
        
        data = messages[j]
        if first_restart:
            data["user_id"] = sender
            first_restart = False  # Set flag to False after the first restart
        else:
            data["user_id"] = random.choice([sender, receiver])
        
        data["conversation_id"] = conversation.id
        Message(**data).save()
        count += 1
    j += 1
    
    user1 = storage.get(User, sender)
    user2 = storage.get(User, receiver)
    if count == 1:
        print(f"        {user1.name} sent a message")
    else:
        print(f"        There are {count} messages between users {user1.name} and {user2.name}")    


user_ids = [user.id for user in user_instances]
initiated = {}
length = len(user_ids)
range_of_values = range(length // 2, length)
rand_range = random.choice(range_of_values)
for i in range(rand_range):
    print(BLUE + f"conversation {i + 1}" + RESET)
    rand_sen_id = random.choice(user_ids)
    rand_rec_id = random.choice(user_ids)
    while rand_sen_id == rand_rec_id:
        rand_rec_id = random.choice(user_ids)
    key_to_check = rand_sen_id
    value_to_check = rand_rec_id
        
    
    if f"[{key_to_check}, {value_to_check}]" not in initiated:
        initiated[f"[{key_to_check}, {value_to_check}]"] = i
    else:
        while f"[{key_to_check}, {value_to_check}]" in initiated:
            rand_sen_id = random.choice(user_ids)
            rand_rec_id = random.choice(user_ids)
            while rand_sen_id == rand_rec_id:
                rand_rec_id = random.choice(user_ids)
            key_to_check = rand_sen_id
            value_to_check = rand_rec_id
        initiated[f"[{key_to_check}, {value_to_check}]"] = i
 
    data = {"sender_id": key_to_check, "receiver_id": value_to_check}
    conversation = Conversation(**data)
    conversation.save()
    
    user1 = storage.get(User, key_to_check)
    user2 = storage.get(User, value_to_check)
    print(f"    {user1.name} initiated a convo with {user2.name}")
    send_msg(conversation)
    print("==========================================================")

print(GREEN + "--all conversations have been initiated--" + RESET)

# for i in range(rand_range):
#     rand_user =
#     users[i].follow()


















print(BLUE + "\n        ALL DATA HAS BEEN GENERATED" + RESET)
print("\n There are:")
print(f"    {storage.count(User)} users")
print(f"    {storage.count(Post)} posts")
print(f"    {storage.count(Comment)} comments")
print(f"    {storage.count(Conversation)} conversations")
print(f"    {storage.count(Message)} messages")
