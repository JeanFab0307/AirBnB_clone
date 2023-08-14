#!/usr/bin/python3
"""Entry point of the command interpreter"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd


memory = storage.all()


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    CLASS_LIST = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place']
    CLASS_LIST.append('Review')

    def do_create(self, cls):
        'Create new instance of a class'
        if not cls:
            print("** class name missing **")
        elif cls not in self.CLASS_LIST:
            print("** class doesn't exist **")
        else:
            eval_obj = str(cls) + "()"
            new_cls = eval(eval_obj)
            new_cls.save()
            print(new_cls.id)

    def do_show(self, arg):
        'Print the string rep of an instance based on the class name and id'
        args = parse(arg)
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in self.CLASS_LIST:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for key, obj in memory.items():
                cls, id = key.split('.')
                if cls == args[0] and id == args[1]:
                    print(obj)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        args = parse(arg)
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in self.CLASS_LIST:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for key, obj in memory.items():
                cls, id = key.split('.')
                if cls == args[0] and id == args[1]:
                    memory.pop(key)
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        'Prints all string rep of all instances based or not on the class name'
        if arg == "":
            for obj in memory.values():
                print(obj)
        elif arg in self.CLASS_LIST:
            for obj in memory.values():
                if obj.__class__.__name__ == arg:
                    print(obj)
        elif arg not in self.CLASS_LIST:
            print("** class doesn't exist **")

    def do_update(self, arg):
        'Updates an instance based on the class name and id'
        args = parse(arg)
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in self.CLASS_LIST:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for key, obj in memory.items():
                cls, id = key.split('.')
                if cls == args[0] and id == args[1]:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        value = update(args)
                        new = {str(args[2]): value}
                        setattr(obj, args[2], value)
                        storage.save()
                    return
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True


def update(args):
    """Do the update command"""
    i = 3
    value = ""
    while i < len(args):
        if i != 3:
            value += " "
        value += str(args[i])
        i += 1
    value = value.split('"')
    val = str(value[1])
    if val.isdigit() is True:
        attr_val = int(val)
    else:
        try:
            attr_val = float(val)
        except Exception:
            attr_val = val
    return attr_val


def parse(arg):
    """Divide a line in a tuple"""
    return tuple(arg.split(" "))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
