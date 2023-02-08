#!/usr/bin/python3
"""console.py program, contains the entry point
    of the command interpreter"""
import cmd
import shlex  # for splitting lines
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
import json


ciara = {"BaseModel": BaseModel,
         "User": User,
         "City": City,
         "Place": Place,
         "Review": Review,
         "State": State,
         "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    """command class"""
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_EOF(self, args):
        "Exit"
        return True

    def do_quit(self, args):
        "Quit command to exit the program\n"
        raise SystemExit

    def do_create(self, args):
        """Creates new instance of BaseModel,
        as long as the given argument is one of the keys,
        and saves new instance in JSON file"""

        if len(args) < 1:
            print("** class name missing **")
        elif args in ciara.keys():
            new = ciara[args]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """do_show prints the string representation
            of an instance

            first it splits args, then checks if
            the input is valid and meets certain
            conditions

            if the input is valid, it searches
            for an instance with the specified class name
            and ID, and prints the content

            if the input is invalid or the instance is not
            found, it prints error messages"""

        split_arg = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif split_arg[0] in ciara.keys():
            if len(split_arg) < 2:
                print("** instance id missing **")
            else:
                search = split_arg[0] + "." + split_arg[1]
                all = storage.all()
                if search in all:
                    print(all[search])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """do_destroy nukes an instance

            first it splits args, then checks if
            the input is valid and meets certain
            conditions

            if the input is valid, it searches
            for an instance with the specified class name
            and ID, and deletes it

            if the input is invalid or the instance is not
            found, it prints error messages

            saves change into the JSON file"""

        split_arg = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif split_arg[0] in ciara.keys():
            if len(split_arg) < 2:
                print("** instance id missing **")
            else:
                search = split_arg[0] + "." + split_arg[1]
                all = storage.all()
                if search in all:
                    del all[search]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """do_all prints all string representation of
            all instances

            first it splits args, then checks if
            the input is valid and meets certain
            conditions

            if the input is valid, it searches
            for an instance with the specified class name
            and ID, and deletes it

            if the input is invalid or the instance is not
            found, it prints error messages

            saves change into the JSON file"""

        split_arg = args.split(" ")
        if len(args) == 0:
            for key in storage.all():
                print([str(storage.all()[key])])
        elif args not in ciara.keys():
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if args == value.__class__.__name__:
                    print([str(storage.all()[key])])

    def do_update(self, args):
        """do_update updates attributes of an instance

            first it splits args, then checks if
            the input is valid and meets certain
            conditions

            if the input is valid, it searches
            for an instance with the specified class name
            and ID, and updates the specified attribute of the instance
            with the given value

            if the input is invalid or the instance is not
            found, it prints error messages

            updated instance is saved in JSON file"""

        split_arg = args.split(" ")
        if len(split_arg) == 0:
            print("** class name missing **")
        elif len(split_arg) < 2:
            print("** instance id missing **")
        elif len(split_arg) < 3:
            print("** attribute name missing **")
        elif len(split_arg) < 4:
            print("** value missing **")
        elif split_arg[0] not in ciara.keys():
            print("** class doesn't exist **")
        else:
            search = split_arg[0] + "." + split_arg[1]
            all = storage.all()
            if search in all:
                setattr(storage.all[search],
                        split_arg[2], split_arg[3].strip('\'"'))
                storage.save()
            else:
                print("** no instance found **")

    """help action is provided by default,
        but should be kept updated and documented
        as we work through tasks"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
