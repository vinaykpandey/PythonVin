#/usr/bin/python
#for i in range(start, stop, step)
def sum_using_recursion(n):
    s = 0
    if(n==1):
        print('if  ===' ,n)
        return n
    else:
        print('else  sss ===',s, ' nnn ===',n)
        s = n + sum_using_recursion(n-1)
        print('else  sss ===',s, ' nnn ===',n)
        return s

N = int(input("Input Number to add: "))
S = sum_using_recursion(N)
print("Sum ===", S)
