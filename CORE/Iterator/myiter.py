class MyIter:

    def __del__(self):
        print('Destructor: ')

    def __init__(self):
        print(" constructor: ")
        self.num = 0

    def __iter__(self):
        print("__iter__: ")
        return self

    def __next__(self):
        print("__next__: ")
        if self.num > 6:
            raise StopIteration
        self.num += 1
        return self.num

obj = MyIter()
print(obj, type(obj))
print(next(obj))
print(next(obj))
it = iter(obj)

print(next(it))
print(next(it))
print(next(it))


print("--------------loop ------------------")
for c in MyIter():
    print(c)