#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBC
    """
    prompt = "(hbnb)"

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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel
        """
        args = arg.split()
        if len(args) == 0:
            print("**class name missing**")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            for key in models.storage.all():
                if len(args) == 0 or args[0] == key.split('.')[0]:
                    print(str(models.storage.all()[key]))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
