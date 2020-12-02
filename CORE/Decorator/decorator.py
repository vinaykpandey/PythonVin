"""
DEF: Decorators provide a simple syntax for calling higher-order functions.
By definition, a decorator is a function that takes another function
and extends the behavior of the latter function without explicitly modifying it.

A rapper around another function

def wrapper(*args, **kwargs):
*args: pass a variable number of arguments to a function

The special syntax **kwargs in function definitions in python is used to pass
 a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).
"""

import time
def time_it_decorator(func):
    def wrapper_function(*args, **kwargs): # wrapper_function(i)
        print('func =',func)
        start = time.time()
        result = func(*args, **kwargs)  # func(i)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*10000) + "mil sec")
        return result
    return wrapper_function #[function in python is first call member/citizen]

#@time_it_decorator
def calculate_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it_decorator
def calculate_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,10)
#out_square = calculate_square(array)
out_cube = calculate_cube(array)
decorated_calculate_square = time_it_decorator(calculate_square)
print(decorated_calculate_square)
#print(decorated_calculate_square)
#decorated_calculate_square(array)
#calculate_cube(array)