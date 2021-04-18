"""
def <func-name> (fargs, *args, **kwargs):
    <statements>
    **kwargs in function definitions in python is used to pass a
     keyworded, variable-length argument list.
"""


def record(**data):
    print(type(data))  # dictionary
    print(data)  # convert key value pair is at dictionary


record(name=['abc', 'xyz'], age=(30, 32))

d = {'name': 'Abc', 'age': '30'}
record(**d)


def hello(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))


hello(name="ABC", age="30")
