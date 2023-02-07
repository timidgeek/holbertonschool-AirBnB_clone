#!/usr/bin/python3
"""console.py program, contains the entry point
    of the command interpreter"""
import cmd
import json
import shlex
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity




our_class = {"BaseModel": BaseModel, "User": User, "City": City,
             "Place": Place, "Review": Review, "State": State, "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    """command class"""
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self, line):
        "Quit command to exit the program\n"
        raise SystemExit

    def do_create(self, args):
        "Creates new instance of BaseModel"
        if len(args) == 0:
            print("** class name missing **")
        elif args in our_class:
            for k, value in our_class.items():
                if k == args:
                    new_instance = our_class[k]()
                storage.save()
                print(new_instance.id)
        else:
            print("** class doesn't exist **")

    """def do_show(self, args):
        "Prints the string representation of an instance"
        if len(args) == 0:
            print("** class name missing **")

    def do_destroy(self, args):
        "Deletes an instance"
        if len(args) == 0:
            print("** class name missing **")

    def do_all(self, args):
        "Prints all string representation of all instances"
        if len(args) == 0:
            print("** class name missing **")

    def do_update(self, args):
        "Updates attributes of an instance"
        if len(args) == 0:
            print("** class name missing **")"""


    """help action is provided by default,
        but should be kept updated and documented
        as we work through tasks"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
