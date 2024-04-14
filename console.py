#!/usr/bin/python3
""" console """

import cmd
import re
import json
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
    print(BLUE + "\t\ttype 'display' to see commands or display <command>" + RESET)

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_display(self, arg):
        """lists all commands and their syntax"""
        mydict = {
        "quit": ["quit - exit console"],
        "create": ["create <class> - creates a class"],
        "show": ["show <class> <id> - displays the specific class"],
        "destroy": ["destroy <class> <id> - destroys the specific class"],
        "all": ["all - lists all classes", "all <class> - lists all specific classes"],
        "update": ["update <class> <id> '<dict>' - updates the class with the kvp of the dict"],
        }
        # ANSI escape code for resetting text color to default
        RESET = "\033[0m"
        # ANSI escape code for green text
        GREEN = "\033[32m"
        
        if len(arg) == 0:
            for value in mydict.values():
                print(GREEN + "\t\t" + "\n\t\t".join(value) + RESET)
        else:
            if arg not in mydict:
                print("Not a valid command")
                return
            print(GREEN + "\t\t" + "\n\t\t".join(mydict[arg]) + RESET)

    def parser(self, args):
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
            new_dict = self.parser(args[1:])
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

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** dict parameter missing, type 'display <update>' to see usage **")
            return
            
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        cls = classes[args[0]]
        id = args[1]
        dict = args[2]
        print(cls, id)
        instance = storage.get(cls, id)

        if instance is None:
            print("** no instance found **")
            return
        
        if not dict:
            print("** attribute name(s) missing **")
            return
        try:
            dict = json.loads(dict)
        except Exception:
            print("Not a valid JSON")
            return

        for key, value in dict.items():
            if not value:
                print("** value missing **\n[try again]")
                return
            setattr(instance, key, value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
