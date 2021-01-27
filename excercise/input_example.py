#!/usr/bin/python
def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
        elif year % 400 == 0:
            leap = True
    return leap


n = input()
input_str = input()
input_list = input_str.split()
input_list = map(int, input_list)
# input_list = [int(x) for x in input_list]
t = tuple(input_list)
print(hash(t))
n = input()
str = input()
lst = str.split()
lst = map(int, lst)
t = tuple(lst)
print(hash(t))

a, b = map(int, input().split() )  # Taking multiple inputs from user in python
