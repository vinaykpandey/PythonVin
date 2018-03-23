#!/usr/bin/env python
'''
Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
print(vars(obj))
print(obj.__dict__)
True/False = isinstance(objName, className) chcek if object is created for class or not
True/False =  issubclass(ChildClass, ParentClass)
'''
class UserProfile:
    name= ''
    age = ''
    collge = ''

    def __init__(self): #constructor
        print(__name__)
        self.name = 'Vinay'
        self.age =  32
        self.collge = 'GLAITM'

    def display_name(self):
        print('Yes')
        #print(self.name)

    def add_user(self, lisUser):
        pass
if __name__ == '__main__':
    obj = UserProfile()
    #print(vars(obj))
    #print(obj.__dict__)
    obj.display_name()


