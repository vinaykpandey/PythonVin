#!/usr/bin/env python
'''include/import a python module and call its
function like: filename.functionname
'''
import stringRev
def reverse(s):
    i =  s[::-1]
    print(i)
    return i


Inputword = input("Enter Word: ")
ReverseStr = stringRev.reverseWord(Inputword)
print('Revered word is: ', ReverseStr)
