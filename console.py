#!/usr/bin/python3
"""AirBnB Console"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']


class HBNBCommand(cmd.Cmd):
    """The command interpreter of AirBnB project"""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Create a new instance of a class and prints the id"""
        if len(args) == 0:
            print("** class name missing **")
        elif args not in classes:
            print("** class doesn't exist **")
        else:
            for i in classes:
                if i == args:
                    a1 = str(args) + '()'
                    a = eval(a1)
            print(a.id)
            a.save()
        pass

    def do_show(self, args):
        """Prints the json file of an instance of a class name and id"""
        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        s = words[0] + '.' + words[1]
        for obj_id in all_objs.keys():
            if s == obj_id:
                obj = all_objs[obj_id]
                print(obj)
                return
        print("** no instance found **")
        pass

    def do_all(self, args):
        """Prints all string representation of all instances"""
        if len(args) == 0:
            all_objs = storage.all()
            new_list = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                new_list.append("{}".format(obj))
            print(new_list)
        elif args not in classes:
            print("** class doesn't exist **")
        elif args in classes:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                key1 = obj_id.split('.')
                if key1[0] == args:
                    obj = all_objs[obj_id]
                    print("{}".format(obj))

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        s = words[0] + '.' + words[1]
        for key, value in all_objs.items():
            if s in key:
                del all_objs[str(s)]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        if len(words) == 3:
            print("** value missing **")
            return
        s1 = words[0] + '.' + words[1]
        all_objs = storage.all()
        for key, value in all_objs.items():
            if s1 in key:
                if len(words) == 2:
                    print("** attribute name missing **")
                    return
                if words[3][0] == "\"" and words[3][-1] == "\"":
                    setattr(value, words[2], words[3][1:-1])
                    storage.save()
                    return
                setattr(value, words[2], words[3])
                storage.save()
                return
        print("** no instance found **")

    def precmd(self, line):
        """
        """
        words = line.split('.', 1)
        if len(words) == 1:
            return cmd.Cmd.precmd(self, line)
        s1 = words[1][:-1].split('(', 1)
        t1 = s1[1].split(', ')
        if s1[1] == '':
            s = s1[0] + ' ' + words[0]
            return cmd.Cmd.precmd(self, s)
        if len(t1) >= 1:
            s = s1[0] + ' ' + words[0] + ' ' + t1[0][1:-1]
        if len(t1) >= 2:
            s = s + ' ' + t1[1][1:-1]
        if len(t1) >= 3:
            if t1[2][0] == "\"" and t1[2][-1] == "\"":
                t1[2] = t1[2][1:-1]
            s = s + ' ' + t1[2]
        return cmd.Cmd.precmd(self, s)

    def do_count(self, line):
        """
        Counts number of instances of a class
        """
        all_objs = storage.all()
        count = 0
        for name in all_objs:
            if name[0:len(line)] == line:
                count += 1
        print(count)

    def emptyline(self):
        """Method called when an empty line is entered in response
        to the prompt"""
        pass

    def do_EOF(self, line):
        """Ctrl D - the program will exit cleanly"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
