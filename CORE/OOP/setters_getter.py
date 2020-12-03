#!/usr/bin/env python
'''
Dynamic setters and getters
'''

externalData = {'name':'Abc'} # Dictionary
attrKeys = ['name', 'age'] # list of property

class Transform(object):


    def __getattribute__(self, name):
       if name in attrKeys:
          # print ('if name in attrKeys')
           return externalData[name]
       #return super(Transform, self).__getattribute__(name)
       return externalData[name]

    def __setattr__(self, name, value):
        if name in attrKeys:
            #print ('if name in attrKeys')
            externalData[name] = value
        else:
            externalData[name] = value
            #super(Transform, self).__setattr__(name, value)

print(externalData)
print(attrKeys)

myInstance = Transform()
myInstance.name = 'Vinay'
myInstance.age = '32'
myInstance.skills = 'Math'
myInstance.grade = 'A+'

print(attrKeys)
print(externalData)
