#!/usr/bin/python

'''
Reduce is a really useful function for performing some computation on a list and returning the result

functool module
'''

from functools import reduce
product = reduce((lambda x, y: x * y), [1,2,3,4,5])
print(product)


