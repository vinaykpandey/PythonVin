#/usr/bin/python
# a = 0
# b = 1
# fibo=[a, b];
# while b < 10:
#      a, b = b, a+b
#      fibo.append(b)
#
# print (fibo)


''' a, b = b, a+b
Explanation
c = a + b
a = b
b = c'''

a = 1
b = 2
fibo=[b];
sum = 2
while b < 4000000:
     a, b = b, a+b
     print("b------: ",b)
     if b < 4000000:
         if b%2 == 0:
            fibo.append(b)
            sum = sum+b
print (fibo)

print("sum====",sum)
