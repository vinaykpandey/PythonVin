# this will calculate the value  of nth element
# frist = 0, second = 1
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        r = Fibonacci(n-1)+Fibonacci(n-2)
        return r

# Driver Program
# use loop to print all element
for i in range(1,10):
    print(Fibonacci(i))
    pass




FibArray = [0, 1]

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib

    # Driver Program


a = fibonacci(9)

print(FibArray)




