'''
We'll see why numpy is very popular and talk about its
main feature "n dimensional array". It is memory efficient,
fast and convenient compared to python native list.
h

'''
import numpy as np
import time
import sys

l = range(1000) # create a list with thousand/1000 element in it

print(sys.getsizeof(5)*len(l)) # here 5 is any number between 0-999 // consume 24000 byte
'''
size of one python object list is 24 byte (64 byte Architecture)
'''

numPyarray = np.arange(1000) # arange is funtion to create array element 0-999 // consume 8000 byte


print(numPyarray.size*numPyarray.itemsize);
'''
size of one  numbpy python object list is 8 byte (64 byte Architecture)
'''
