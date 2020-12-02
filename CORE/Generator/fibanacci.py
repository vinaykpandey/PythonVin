'''
simple way to create iterator
yield is like return but some difference,  preserve the state of last execution
'''
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for f in fib():
    if f > 100:
        break
    print(f)
