import time


def fact(x):
    print('x', x, ' in loop ==', x)
    if x == 1:
        return 1
    else:
        time.sleep(2)
        s = x * fact(x - 1)
        print('temp result', x, '  ==', s)
        return s


result = fact(3)
print(result)
