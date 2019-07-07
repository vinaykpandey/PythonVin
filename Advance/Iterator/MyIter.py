class MyIter():
    def __init__(self):
        print("inside init")
    def __iter__(self):
        return self

    def next(self):
        return self

r = MyIter()
itr = iter(r)
print(itr)
print(next(itr))
print(next(itr))