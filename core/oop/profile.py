from .decorator import message

print(message)
'''
Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
print(vars(obj))
print(obj.__dict__)
True/False = isinstance(objName, className) chcek if object is created for class or not
True/False =  issubclass(ChildClass, ParentClass)
'''


class UserProfile:
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

    def display_name(self):
        # print('Yes')
        print(self.name)

    def add_user(self, user_list):
        pass


if __name__ == '__main__':
    obj = UserProfile()
    print(vars(obj))
    # print(obj.__dict__)
    obj.display_name()
