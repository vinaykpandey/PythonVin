from message_decor import message

print(message)
'''
Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
print(vars(obj))
print(obj.__dict__)
True/False = isinstance(objName, className) chcek if object is created for class or not
True/False =  issubclass(ChildClass, ParentClass)
'''


class UserProfile:
    """
    doing some poc
    """
    decorators = [message]

    name = ''
    age = ''
    college = ''
    address = ''

    def __init__(obj_self):  # constructor
        print(obj_self)
        # print(__name__)
        obj_self.name = 'Vinay'
        obj_self.age = 32
        obj_self.college = 'GLAITM'

    def set_name(obj_self):
        # print('Yes')
        print(obj_self.name)

    def get_name(self):
        print(self.name)


if __name__ == '__main__':
    obj = UserProfile()
    print(vars(obj))
    # print(obj.__dict__)
    obj.get_name()
    obj.name = "Dev"
    obj.get_name()
