#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import sys

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_
    """

    if sys.stdin and sys.stdin.isatty():
        prompt = "(hbnb) "
    else:
        prompt = "(hbnb) \n"

    def do_EOF(self, args):
        """Ctrl + D quit the program"""
        return True

    def do_quit(self, args):
        """use to exit the program"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, arg):
        """Create instance specified by user"""
        if self.checkClassName(arg) is False:
            return False

        args = arg.split()
        className = args[0]

        model = globals()[className]()
        model.save()
        print(model.id)
        return True

    def do_show(self, arg):
        """Print string representation: name and id"""
        if self.checkClassName(arg) is False:
            return False

        args = arg.split()
        className = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return False

        classId = className+"."+args[1]
        for key, value in storage.all().items():
            if key == classId:
                print(value.__str__())
                return True

        print("** no instance found **")
        return False

    def do_destroy(self, arg):
        """Destroy instance specified by user; Save changes to JSON file"""
        if self.checkClassName(arg) is False:
            return False

        args = arg.split()
        className = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return False

        classId = className+"."+args[1]
        for key, value in storage.all().items():
            if key == classId:
                storage.delete(value)
                storage.save()
                return True

        print("** no instance found **")
        return False

    def do_all(self, arg):
        """Print all objects or all objects of a specific class"""
        args = arg.split()
        instances = []

        if len(args) < 1:
            for key, value in storage.all().items():
                instances.append(value.__str__())
        else:
            className = args[0]

            if className not in globals():
                print("** class doesn't exist **")
                return False

            for key, value in storage.all().items():
                if value.__class__.__name__ == className:
                    instances.append(value.__str__())

        print(instances)

    def do_update(self, arg):
        """Updates an object, must be an exact attribute"""
        if self.checkClassName(arg) is False:
            return False

        args = arg.split()
        className = args[0]
        exists = False
        obj = None

        if len(args) < 2:
            print("** instance id missing **")
            return False

        classId = className+"."+args[1]
        for key, value in storage.all().items():
            if key == classId:
                exists = True
                obj = value

        if exists is False:
            print("** no instance found **")
            return False

        if len(args) < 3:
            print("** attribute name missing **")
            return False

        if len(args) < 4:
            print("** value missing **")
            return False

        obj.__setattr__(args[2], args[3])
        storage.new(obj)
        storage.save()

    @classmethod
    def checkClassName(self, arg):
        """check class if name:"""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return False

        className = args[0]

        if className not in globals():
            print("** class doesn't exist **")
            return False

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
