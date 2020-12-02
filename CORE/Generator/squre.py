def square(lista):
    for x in lista:
        yield x*x

s = square([1,2,3,4])
print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))