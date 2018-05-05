'''
iterable vs iterator

iterable => Object (e.g:  lists, string, tuple, files etc)
Iterable are capable of create iterator
__iter__   (iter method)
we cane check dir(list), there is __iter__ method written

listone = [1,2,3]
listtwo = [4,5,6]

mergedlist = listone + listtwo

Output:
mergedlist
[1,2,3,4,5,6]



The usual way is to use zip():

for x, y in zip(a, b):
    # x is from a, y is from b

This will stop when the shorter of the two iterables a and b is exhausted.
Also worth noting: itertools.izip() (Python 2 only) and itertools.izip_longest() (itertools.zip_longest() in Python 3).

chain(l1,l2,l3)
'''
# from itertools import *


l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
# for i in chain(l1,l2):
# pass
# print i


iterable = iter(range(15))
for i in iterable:
    # print('strat ==== ', i)
    if i == 5:
        [iterable.next() for x in range(1)]
    print('= ====', i)
    # print(iterable.next(i))
