#!/usr/bin/python3
""" console """

import cmd
import re
from datetime import datetime, date
import models
from models import storage
from models.base_model import BaseModel
from models.base_model2 import BaseModel2
from models.user import User
from models.post import Post
from models.comment import Comment
from models.feedback import Feedback
from models.reported_post import ReportedPost
from models.conversation import Conversation
from models.message import Message
from models.reported_user import ReportedUser
from models.reported_message import ReportedMessage
from models.reported_comment import ReportedComment

import shlex  # for splitting the line along spaces except in double quotes


classes = {"User": User, "Post": Post, "Comment": Comment,
           "ReportedPost": ReportedPost, "feedback": Feedback,
           "Conversation": Conversation, "Message": Message, "ReportedUser": ReportedUser,
           "ReportedComment": ReportedComment, "ReportedMessage": ReportedMessage}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    # ANSI escape code for blue text
    BLUE = "\033[34m"
    # ANSI escape code for resetting text color to default
    RESET = "\033[0m"
    prompt = 'Ikiru' + BLUE + '$ ' + RESET

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if key == "dob":
                    match = re.match(r'"date\((\d+),_(\d+),_(\d+)\)"', value)
                    if match:
                        year, month, day = map(int, match.groups())
                        value = date(year, month, day)
                        
                    else:
                        raise ValueError("Invalid date string format. expected: %Y %m %D")
                elif value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """
        Creates a new instance of a class
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                instances = storage.all(classes[args[0]])
                if key in instances:
                    print(instances[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                instance = storage.all(classes[args[0]])
                if key in instance:
                    storage.delete(instance[key])
                    storage.save()
                    print("Instance has been deleted")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    # do_update

if __name__ == '__main__':
    HBNBCommand().cmdloop()
