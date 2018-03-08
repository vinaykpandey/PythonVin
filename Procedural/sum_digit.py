#/usr/bin/python
import sys
'''
 	a // b =>>>> floordiv(a, b)
 	a  = a//b
'''
def sum_digits(n):
    s = 0
    while (n > 0):
        s += n % 10
        n //= 10
        print ("Floor quotient :", n)
        print ("\n")
    return s

if __name__ == "__main__":
    number = int(input("Enter your number "))
    total = sum_digits(number)
    print ("The total sum of digits is:", total)


