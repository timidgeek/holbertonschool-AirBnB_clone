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
        "Creates new instance of BaseModel"
        if len(args) < 1:
            print("** class name missing **")
        elif args in ciara.keys():
            new = ciara[args]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        "Prints the string representation of an instance"
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
        """Deletes an instance based on the
            class name and id, and saves the
            change into the JSON file"""

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
        "Prints all string representation of all instances"
        split_arg = args.split(" ")
        if len(args) == 0:
            for k in storage.all():
                print([str(storage.all()[k])])
        elif args not in ciara.keys():
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if args == v.__class__.__name__:
                    print([str(storage.all()[k])])

    def do_update(self, args):
        "Updates attributes of an instance"
        if len(args) == 0:
            print("** class name missing **")

        split_arg = args.split(" ")
        if len(split_arg) == 0:
            print("** class name missing **")
        elif len(split_arg) < 2:
            print("** instance id missing **")
        elif len(split_arg) < 3:
            print("** attribute name missing **")
        elif len(split_arg) < 4:
            print("** value missing **")
        elif split_arg[0] not in ciara:
            print("** class doesn't exist **")
        else:
            search = split_arg[0] + "." + split_arg[1]
            all = storage.all()
            for search in all:
                if search in all:
                    setattr(storage.all[search],
                            split_arg[2], split_arg[3])
                    storage.save()
            else:
                print("** no instance found **")

    """help action is provided by default,
        but should be kept updated and documented
        as we work through tasks"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
