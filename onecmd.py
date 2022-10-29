# #  for testing purposes
# import re

# def onecmd(self, line):
#     if "." in line:
#         line = re.split(r"(\w+)\.", line)
#         print(line)
#         return
#         #  check what type of command was passed
#         if command[:3] == "all" or command[:5] == "count":
#             command = command.replace("(", "").replace(")", "")
#             line = f"{command} {class_name}"
#         elif command[:4] == "show" or command[:7] == "destroy":
#             #  command = show(<id>)
#             # replace (" and ") from the command
#             command = command.replace('("', ' ').replace('")', '')
#             #  split the above command into the command and the id
#             command, instance_id = command.split(" ")
#             #  generate the actual line (command class_name id)
#             line = f"{command} {class_name} {instance_id}"
#         elif command[:6] == "update":
#             #  check which format of update was used
#             if "{" in command:
#                 # (\w+)\.(\w+)\(\"([a-zA-Z0-9\-]+)\"\,\s(\{[\'a-zA-Z\_\s\:\"\,0-9]+\})
#                 #  class_name command id dictionary
#                 #  <class name>.update(<id>, <dictionary representation>)
#                 # command = command.replace('("', ' ').replace(')', '')
#                 class_name = re.split(r"(\w+)\.(\w+)\(\"([a-zA-Z0-9\-]+)\"\,\s(\{[\'a-zA-Z\_\s\:\"\,0-9]+\})", line)
#                 # command, instance_id = command_id.split(' ')
#                 class_name, command, instance_id, update_dict = class_name[1], class_name[2], class_name[3], class_name[4]

#                 print(class_name, command, instance_id, update_dict)

#                 for key, value in update_dict.items():
#                     line = f"{command} {class_name} {instance_id} {key} {value}"
#                     cmd.Cmd.onecmd(self, line)
#                 return
#             # User.update("44006e6e-8cf7-4560-a22c-138125c159ca", {'id': "44006e6e-8cf7-4560-a22c-138125c159ca", "first_name": "Tony", "email": "obed@gmail.com"})

#             else:
#                 # <class name>.update(<id>, <attribute name>, <attribute value>)
#                 command = command.replace('("', ' ').replace('")', '')

#                 command, instance_id, attr_name, value = re.split(' |", "', command)
#                 line = f"{command} {class_name} {instance_id} {attr_name} {value}"
#     # return cmd.Cmd.onecmd(self, line)
#     # print(line)
#     # print(command, instance_id, attr_name, value )


#     def onecmd(self, line):
#         # check if this line matches the given pattern
#         if re.match(r"^(\w+)\.(\w+)\(:?.*\)$", line) is not None:
#             # print("There was a match")
#             # let's break line into class name and command_line
#             line = re.split(r"^(\w+)\.(\w+\(.*\))$", line)
#             class_name, command_line = line[1], line[2]
#             # print(class_name, command_line)

#             #  check what type of command was passed
#             if command_line[:3] == "all" or command_line[:5] == "count":
#                 command = command_line.replace("(", "").replace(")", "")
#                 line = f"{command} {class_name}"
#                 # print(line)
#             elif command_line[:4] == "show" or command_line[:7] == "destroy":
#                 # replace (" and ") from the command
#                 command = command_line.replace('("', ' ').replace('")', '')
#                 #  split the above command into the command and the id
#                 command, instance_id = command.split(" ")
#                 #  generate the actual line (command class_name id)
#                 line = f"{command} {class_name} {instance_id}"
#             elif command_line[:6] == "update":
#                 # which update format was used
#                 if re.match(r"^(\w+\(.*\{.*\}\))$", command_line):
#                     #  using the dictionary format
#                     print(command_line)
#                     command_line = re.split(r"^(\w+)\([\"\']([a-zA-Z0-9\-]+)[\"\']\,\s(\{[\'a-zA-Z\_\s\:\"\,0-9]+\})$", command_line)
#                     print(command_line)
#                     # command, instance_id, update_dict = class_name[1], class_name[2], class_name[3]
#                     # line = f"{command} {class_name} {instance_id} {update_dict}"
#                     # print(line)

#                 else:
#                     # using the regular update format
#                     command_line = re.split(r"^(\w+)\([\"\'](.+?)[\"\']\,\s?[\"\'](.+?)[\"\']\,\s?[\"\']?(.+?)[\"\']?\)$", command_line)
#                     # print(command_line)

#                     command, instance_id, attribute, value = command_line[1], command_line[2], command_line[3], command_line[4]
#                     line = f"{command} {class_name} {instance_id} {attribute} {value}" 
#                     print(line) 
#             # return cmd.Cmd.onecmd(self, line)
#         else:
#             # return the default onecmd implementation
#             # return cmd.Cmd.onecmd(self, line)
#             print("There was no match")


# #!/usr/bin/python3
# '''Command Line Interpreter'''
# import cmd
# from models import storage
# from models import *
# import re
# import sys
# import json

# class HBNBCommand(cmd.Cmd):
#     prompt = "(hbnb)"

#     def do_EOF(self, *args):
#         '''End of file command to exit the program'''
#         return True

#     def do_quit(self, *args):
#         '''Quit command to exit the program'''
#         quit()
    
#     def do_create(self, line):
#         '''Create a new instance called <name>'''
#         if line != "" or line is not None:
#             if line not in storage.classes():
#                 print("** class doesn't exist **")
#             else:
#                 # create an instance of the given class
#                 obj_intance = storage.classes()[line]()
#                 obj_intance.save()
#                 print(obj_intance.id)
#         else:
#             print("** class name missing **")
    
#     def do_show(self, line):
#         # check if class name and instance id was provided
#         if line == "" or line is None:
#             print("** class name missing **")
        
#         else:
#             # get all the arguments passed via the command line
#             class_info = line.split(" ")
#             if len(class_info) < 2:
#                 print("** instance id missing **")
#             else:
#                 class_name = class_info[0]
#                 instance_id = class_info[1]
#                 # check if class name exists
#                 if class_name in storage.classes():
#                     # check if instance_id exists
#                     key = f"{class_name}.{instance_id}"
#                     if key not in storage.all():
#                         print("** no instance found **")
#                     else:
#                         instance_dict = storage.all()[key]
#                         print(instance_dict)
                    
#                 else:
#                     print("** class doesn't exist **")

#     def do_destroy(self, line):
#         # check if class name and instance id was provided
#         if line == "" or line is None:
#             print("** class name missing **")
        
#         else:
#             # get all the arguments passed via the command line
#             class_info = line.split(" ")
#             if len(class_info) < 2:
#                 print("** instance id missing **")
#             else:
#                 class_name = class_info[0]
#                 instance_id = class_info[1]
#                 # check if class name exists
#                 if class_name in storage.classes():
#                     # check if instance_id exists
#                     key = f"{class_name}.{instance_id}"
#                     if key not in storage.all():
#                         print("** no instance found **")
#                     else:
#                         # delete this instance and save to json
#                         del storage.all()[key]
#                         storage.save()
#                         return
                        
                    
#                 else:
#                     print("** class doesn't exist **")

#     def do_all(self, line):
#         instance_obj = storage.all()
#         instance_list = []
        
#         if line == "" or line is None:
#             for key, value in storage.all().items():
#                 instance_list.append(str(value))
#             print(instance_list)

#         else:
#             if line not in storage.classes():
#                 print("** class doesn't exist **")
#                 return
#             else:
#                 for key, value in storage.all().items():
#                     class_name, instance_id = key.split(".")
#                     if line == class_name:
#                         instance_list.append(str(value))
#                 print(instance_list)

#     def do_update(self, line):
#         # check if matches dictionary format
#         if re.match(r"\w+\(\".+?\"\,\s?\{.*?}\)", line) is not None:
#             # split the dictionary
#             line = list(filter(None, re.split(r"^(\w+)\(\"(.+?)\"\,\s?(\{.*?})\)$", line)))
#             print(line)
#             #  validation of inputs
#             if len(line) == 0:
#                 print("** class name missing **")
#             elif len(line) == 1:
#                 print("** instance id missing **")
#             elif len(line) == 2:
#                 print("** attribute name missing **")
#             else:
#                 class_name, instance_id, update_dict = line[0], line[1], line[2]
#                 if class_name not in storage.classes():
#                     print("** class doesn't exist **")
#                 else:
#                     key = f"{class_name}.{instance_id}"
#                     if key not in storage.all():
#                         print("** no instance found **")
#                     else:
#                         instance_dict = storage.all()[key]
#                         update_dict = json.loads(update_dict)
#                         print(type(update_dict))
#                         for key, value in update_dict.items():
#                             value = type(key)(value)
#                             # setattr(instance_dict, key, value)
#                             print(type(key))
#                             print(key, value)

#             return
#         else:
#             # split the other format
#             line = list(filter(None, re.split(r"(\w+)\(\"(.+?)\"\,\s?\"(.+?)\"\,\s?\"(.+?)\"\)", line)))
#             print(line)
#             return


#         args = line.split(" ")
#         if line == "" or line is None:
#             print("** class name missing **")
#             return
#         if len(args) == 1:
#             print("** instance id missing **")
#             return
#         if len(args) == 2:
#             print("** attribute name missing **")
#             return
#         if len(args) == 3:
#             print("** value missing **")
#             return
#         if len(args) > 2:
#             # check whether the simple format or the dictionary format
#             print(line)
#             return
#             (class_name, instance_id, attribute, value) = line.split(" ")
#             # print(class_name, instance_id, attribute, value)
#             #  check if class exists
#             if class_name not in storage.classes():
#                 print("** class doesn't exist **")
#             else:
#                 key = f"{class_name}.{instance_id}"
#                 if key not in storage.all():
#                     print("** no instance found **")
#                 else:
#                     instance_dict = storage.all()[key]
#                     # remove quotation marks on value
#                     if '"' in value:
#                         value = value.replace('"', '')
#                     # update attributes in the instance dictionary
#                     value = type(attribute)(value)
#                     setattr(instance_dict, attribute, value)
#                     storage.save()

#     def update_dict(line):
#         #  command class_name id {dict}
#         # use set attribute
#         # for key, value in dict.items:
#         #     value = type(key)(value)
#         #     setattr(instance_dict, key, value)
#         pass

#     def emptyline(self):
#         pass
    
#     def precmd(self, line):
#         # make the app work non-interactively
#         if not sys.stdin.isatty():
#             print()
        
#         # check the args that were submitted
#         # checks = re.match(r"^(\w+)\.(\w+)\(:?.*\)$", line)
#         # if checks is not None:
#         #     line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ').replace(",", "")
#         #     print(line)
#         #     line = line.split() # split into various parts
            
#         #     if line[1][:3] == "all" or line[1][:5] == "count":
#         #         # line[0], line[1] = line[1], line[0]
#         #         print("all or count")

#         #     elif line[1][:4] == "show" or line[1][:7] == "destroy":
#         #         line[2] = line[2].replace("\"", "")
            
#         #     elif line[1][:6] == "update":
#         #         new_line = []
#         #         print("Update")
#         #         # check if simple format or dictionary format
#         #         # if re.match(r"", line) is not None:
#         #         #     pass
#         #         # # if the simple format
#         #         # else:
#         #             # for arg in line:
#         #             #     arg = arg.replace(",", "")
#         #             #     new_line.append(arg)
#         #             # line = new_line
#         #         print(line)

#         #     line[0], line[1] = line[1], line[0]
#         #     line = " ".join(line)

#         # print(checks)
#         # print(line)

#         return cmd.Cmd.precmd(self, line)

#     def do_count(self, line):
#         # line => User
#         count = 0
#         for key in storage.all().keys():
#             class_name, instance_id = key.split(".")
#             if line == class_name:
#                 count += 1
#         print(count)

# if __name__ == '__main__':
#     HBNBCommand().cmdloop()


#     # check the args that were submitted
#         # checks = re.match(r"^(\w+)\.(\w+)\(:?.*\)$", line)
#         # if checks is not None:
#         #     line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ').replace(",", "")
#         #     print(line)
#         #     line = line.split() # split into various parts
            
#         #     if line[1][:3] == "all" or line[1][:5] == "count":
#         #         # line[0], line[1] = line[1], line[0]
#         #         print("all or count")

#         #     elif line[1][:4] == "show" or line[1][:7] == "destroy":
#         #         line[2] = line[2].replace("\"", "")
            
#         #     elif line[1][:6] == "update":
#         #         new_line = []
#         #         print("Update")
#         #         # check if simple format or dictionary format
#         #         # if re.match(r"", line) is not None:
#         #         #     pass
#         #         # # if the simple format
#         #         # else:
#         #             # for arg in line:
#         #             #     arg = arg.replace(",", "")
#         #             #     new_line.append(arg)
#         #             # line = new_line
#         #         print(line)

#         #     line[0], line[1] = line[1], line[0]
#         #     line = " ".join(line)

#         # print(checks)
#         # print(line)

#         #  here is the working do_update() method
#         def do_update(self, line):
#         # check if matches dictionary format
#         if re.match(r"\w+\(\".+?\"\,\s?\{.*?}\)", line) is not None:
#             # split the dictionary
#             line = list(filter(None, re.split(r"^(\w+)\(\"(.+?)\"\,\s?(\{.*?})\)$", line)))
#             print("It is")
#             #  validation of inputs
#             if len(line) == 0:
#                 print("** class name missing **")
#             elif len(line) == 1:
#                 print("** instance id missing **")
#             elif len(line) == 2:
#                 print("** attribute name missing **")
#             else:
#                 class_name, instance_id, update_dict = line[0], line[1], line[2]
#                 if class_name not in storage.classes():
#                     print("** class doesn't exist **")
#                 else:
#                     key = f"{class_name}.{instance_id}"
#                     if key not in storage.all():
#                         print("** no instance found **")
#                     else:
#                         instance_dict = storage.all()[key]
#                         update_dict = json.loads(update_dict)

#                         attributes = storage.attributes()[class_name]
#                         # print(attributes)
#                         for key, value in update_dict.items():
#                             if key in attributes:
#                                 # print(key)
#                                 value = attributes[key](value)
#                                 # print(attributes[key])
#                                 setattr(instance_dict, key, value)
#                                 storage.save()
#         else:
#             print("not a dictionary")
#             # split the other format
#             line = list(filter(None, re.split(r"(\w+)\(\"(.+?)\"\,\s?\"(.+?)\"\,\s?\"(.+?)\"\)", line)))
#             #  validation of inputs
#             if len(line) == 0:
#                 print("** class name missing **")
#             elif len(line) == 1:
#                 print("** instance id missing **")
#             elif len(line) == 2:
#                 print("** attribute name missing **")
#             else:
#                 class_name, instance_id, attribute, value = line[0], line[1], line[2], line[3]
#                 #  check if class exists
#                 if class_name not in storage.classes():
#                     print("** class doesn't exist **")
#                 else:
#                     key = f"{class_name}.{instance_id}"
#                     if key not in storage.all():
#                         print("** no instance found **")
#                     else:
#                         instance_dict = storage.all()[key]
#                         # update attributes in the instance dictionary
#                         value = type(attribute)(value)
#                         setattr(instance_dict, attribute, value)
#                         storage.save()