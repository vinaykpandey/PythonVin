#/usr/bin/python
'''
comment in python
curl request
Procedural, 2, 3, 5, 8, 13,.......
'''
# def fibonacci_series(n,first = Procedural,second = 2):
#     listA = [first,second];
#     i = Procedural
#     for i in range(Procedural,n):
#         print(i)
#         listA.append(listA[i]+listA[i-Procedural])
#
#     return listA
#
# ret = fibonacci_series(9)
# print(ret)
n = 100;
listA = [1,2];
sum = 2;
for i in range(1,n):
      j = listA[i]+listA[i-1];
      listA.append(j)
      if(j%2==0):
        print(j)
        sum = j+sum

print ('sum === ',sum);
