#!/usr/bin/python3
"""
Entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBC
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line + enter
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
