'''
iter.__doc__
'iter(collection) -> iterator\niter(callable, sentinel) -> iterator\n\nGet an iterator from an
object.  In the first form, the argument must\nsupply its own iterator,
 or be a sequence.\nIn the second form, the callable is called until it returns the sentinel.'
'''
class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","cnn","abc","espn"]
        self.index = -1

    def __iter__(self):
        return self

    def next(self):
        self.index += 1
        if self.index == len(self.channels):
            raise Exception('StopIteration')
        return self.channels[self.index]

r = RemoteControl()
itr=iter(r)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

'''

You're using Python 2.x, which has used .next() since forever and still does so - only Python 3 renamed that method to .__next__(). Python 2 and 3 aren't compatible. If you're reading a 3.x book, use Python 3.x yourself, and vice versa.

For Python 2.x, you can change __next__() to next()

'''


