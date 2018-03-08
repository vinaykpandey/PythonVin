#/usr/bin/python
import dis
import sys
x = int(input('Enter your x: '))
y = int(input('Enter your y: '))

'''without using third variable'''
x = x+y
y = x-y
x = x-y
print ('x===',x, 'y=====',y)

'''using third variable'''
temp = x
x = y
y = temp

print ('x===',x, 'y=====',y)

'''inbuilt expression '''
x,y = y,x

print ('x===',x, 'y=====',y)

