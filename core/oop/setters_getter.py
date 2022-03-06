"""
Dynamic setters and getters
"""

external_data = {'name': 'Abc'}  # Dictionary
attr_keys = ['name', 'age']  # list of property


class Transform(object):

    def __getattribute__(self, name):
        if name in attr_keys:
            # print ('if name in attrKeys')
            return external_data[name]
        # return super(Transform, self).__getattribute__(name)
        return external_data[name]

    def __setattr__(self, name, value):
        if name in attr_keys:
            # print ('if name in attrKeys')
            external_data[name] = value
        else:
            external_data[name] = value
            # super(Transform, self).__setattr__(name, value)


print(external_data)
print(attr_keys)

my_instance = Transform()
my_instance.name = 'Vinay'
my_instance.age = '32'
my_instance.skills = 'Math'
my_instance.grade = 'A+'

print(attr_keys)
print(external_data)
