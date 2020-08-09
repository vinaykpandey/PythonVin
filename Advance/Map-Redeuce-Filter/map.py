#!/usr/bin/python
'''
map(aFunction, aSequence) /// map(func, iter)

map take 2 arg, 1- a function, 2 - Iterable Object (list, tuple, set, dict).
Here Function apply on each element of list/tuple/..


'''
import math

def area(r):
    """Area of a circle with radius 'r' """
    return math.pi * (r**2)


# eample
radi_data = [2,4,5,7,8,9]

#solution

#method 1: Direct iteration using loop
areas_data = []
for r in radi_data:
    A = area(r)
    areas_data.append(A)

print (areas_data) # o/p 1

# Method 2: Use 'map' function
# its a mapped object,  then we need to convert to list, map fn return iterator over each
map(area, radi_data)
list(map(area, radi_data) ) # o/p 2