#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import shlex
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def help_quit(self):
        """Help message for quit command."""
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id.

        Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id.

        Ex: $ show BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        try:
            cls_name = args[0]
            obj_id = args[1]
            obj_key = "{}.{}".format(cls_name, obj_id)
            obj = models.storage.all().get(obj_key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.

        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        try:
            cls_name = args[0]
            obj_id = args[1]
            obj_key = "{}.{}".format(cls_name, obj_id)
            objects = models.storage.all()
            if obj_key in objects:
                del objects[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the
        class name.

        Ex: $ all BaseModel or $ all.
        """
        objects = models.storage.all()
        if arg:
            try:
                obj_list = [str(v) for k, v in objects.items()
                            if v.__class__.__name__ == arg]
            except AttributeError:
                print("** class doesn't exist **")
                return
        else:
            obj_list = [str(v) for k, v in objects.items()]
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute.

        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        try:
            cls_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
            obj_key = "{}.{}".format(cls_name, obj_id)
            objects = models.storage.all()
            if obj_key not in objects:
                print("** no instance found **")
                return
            obj = objects[obj_key]
            setattr(obj, attr_name, attr_value)
            models.storage.save()
        except IndexError:
            print("** instance id missing **")
        except AttributeError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
