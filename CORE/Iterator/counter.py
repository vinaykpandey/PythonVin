class Counter:
    def __init__(self):
        self.current = 3
        self.high = 10

    def __iter__(self):
        return self

    def __next__(self): # Python 2: def next(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for c in Counter():
    print(c)