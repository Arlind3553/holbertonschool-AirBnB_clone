#!/usr/bin/python3
"""
Entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def EOF(self, arg):
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