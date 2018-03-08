#!/usr/bin/env python
'''
pass: Suppose you are designing a new class with some methods that you don't want to implement, yet.
s = "VINAY"
str = ""
for i in s:
    print('current str ==', str ,' iiii char =====', i)
    str = i + str
    print('new str ==', str)

'''
def reverseWord(ActualString):
    pass
    revString = ''
    maxIndex = len(ActualString)
    for i in range(0, maxIndex):
        revString = revString +  ActualString[maxIndex - i -1]
    return revString

if __name__ == "__main__":
    Inputword = input("Enter Word: ")
    ReverseStr = reverseWord(Inputword)
    print('Revered word is: ', ReverseStr)
