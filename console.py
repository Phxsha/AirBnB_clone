#!/usr/bin/python3
"""
Defines the HBNBCommand class, a command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBnB project.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self):
        """
        Help message for quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exit the program gracefully on EOF.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

