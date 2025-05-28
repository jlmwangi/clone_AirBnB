#!/usr/bin/python3
'''the entry point of the commane interpreter'''

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter, console to manage airbnb classes"""
    prompt = '(hbnb) '


    def emptyline(self):
        '''called when an empty line is entered'''
        pass

    def do_quit(self, arg):
        '''exit program'''
        return True

    def do_EOF(self, arg):
        '''exits program too'''
        return True

    def do_create(self, arg):
        '''creates a new instance of BaseModel, saves it and prints the id'''
        if arg:
            if arg == 'BaseModel':
                from models.base_model import BaseModel
                base_model = BaseModel()
                base_model.save()
                print(f"{base_model.id}")
            elif arg == 'User':
                from models.user import User
                user = User()
                user.save()
                print(f"{user.id}")
            elif arg == 'Place':
                from models.place import Place
                place = Place()
                place.save()
                print(f"{place.id}")
            elif arg == 'State':
                from models.state import State
                state = State()
                state.save()
                print(f"{state.id}")
            elif arg == 'City':
                from models.city import City
                city = City()
                city.save()
                print(f"{city.id}")
            elif arg == 'Amenity':
                from models.amenity import Amenity
                amenity = Amenity()
                amenity.save()
                print(f"{amenity.id}")
            elif arg == 'Review':
                from models.review import Review
                review = Review()
                review.save()
                print(f"{review.id}")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            return


    def do_show(self, args):
        '''prints string rep of an instance based on class name and id'''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models import storage

        class_names = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        if len(parts) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = parts[0], parts[1]

        if class_name not in class_names:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key in objects:
            print(str(objects[key]))
        else:
            print("** no instance found **")
            return
         

    def do_destroy(self, args):
        '''deletes an instance based on class name and id'''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models import storage

        class_names = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        if len(parts) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = parts[0], parts[1]

        if class_name not in class_names:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")
            return
            
    def do_all(self, arg=None):
        '''prints string representation of all instances based or not on the class name
           result must be a list of strings
        '''
        from models import storage
        from models.user import User
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        
        list_str = []
        if arg:
            class_names = ["BaseModel", 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
            if arg in class_names:
                objects = storage.all()
                for key, obj in objects.items():
                    if key.startswith(f"{arg}."):
                        list_str.append(str(obj))
                print(list_str)
            else:
                print("** class doesn't exist **")
                return
        else:
            objects = storage.all()
            for key, obj in objects.items():
                list_str.append(str(obj))
            print(list_str)

    def do_update(self, args):
        '''Updates an instance based on the class name and id by adding or updating attribute
           Usage: update <class name> <id> <attribute name> "<attribute value>"
        '''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review 
        from models import storage

        class_names = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        if len(parts) < 2:
            print("** instance id missing **")
            return
        elif len(parts) < 3:
            print("** attribute name missing **")
            return
        elif len(parts) < 4:
            print("** value missing **")
            return
        else:
            class_name, instance_id, attr_name, attr_value = parts[0], parts[1], parts[2], parts[3]

            if class_name not in class_names:
                print("** class doesn't exist **")
                return

            key = f"{class_name}.{instance_id}"
            objects = storage.all()

            if key in objects:
                obj = objects[key]

                if attr_value.startswith('"') and attr_value.endswith('"'):
                    attr_value = attr_value[1:-1]

                if attr_value.isdigit():
                    attr_value = int(attr_value)
                elif attr_value.isdigit() and '.' in attr_value:
                    attr_value = float(attr_value)
                elif attr_value.lower() in ("true", "false"):
                    attr_value = attr_value.lower() == "true"

                setattr(obj, attr_name, attr_value)
                storage.save()
            else:
                print("** no instance found **")
                return         




if __name__ == "__main__":
    HBNBCommand().cmdloop()
