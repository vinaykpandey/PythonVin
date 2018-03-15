#/usr/bin/python
import sys
'''
 	a // b =>>>> floordiv(a, b)
 	a  = a//b
 	 n //= i
 	 n = n//i
'''

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        #print ('iiiiii===', i)
        if n % i:
            #print ('inininini===', i)
            i += 1
        else:
            n //= i
           # print ('nnnn===', n)
    return n

number = int(input("Enter your number: "))
s = largest_prime_factor(number)
print ('largest prime factor is: ',s);
