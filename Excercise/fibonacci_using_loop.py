# /usr/bin/python
"""
f, s, n
f -  first element
s - second element
n - length of fibonacci series
"""


def fibonacci_series(n, first=4, second=5):
    lista = [first, second]  # first and second element
    for i in range(1, n - 1):
        e = lista[i] + lista[i - 1]
        lista.append(e)
    return lista


ret = fibonacci_series(9, 0, 1)
print("Total number in the fibonacci series: ", len(ret))
print(ret)
