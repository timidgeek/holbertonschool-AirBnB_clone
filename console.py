#!/usr/bin/python3
"""console.py program, contains the entry point
    of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    while input == "":
        pass

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self, line):
        "Quit command to exit the program\n"
        raise SystemExit

    """help action is provided by default,
        but should be kept updated and documented
        as we work through tasks"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
