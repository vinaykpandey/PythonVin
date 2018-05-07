'''
lambda is anonymous function

lambda arguments : expression
single line expression
'''


def sum_num(x, y):
    #using user defined function
    return x + y


# Call the function
s = sum_num(2, 3)  # Output: 5

print('Sum of number is:{sum}'.format(sum=s))

#using lambda
'''
n lambda x, y: x + y; x and y are arguments to the function and x + y is the expression which gets executed and its values is returned as output.

lambda x, y: x + y returns a function object which can be assigned to any variable, in this case function object is assigned to the add variable.'''

sum_num = lambda x, y : x + y
print sum_num(2, 3) # Output: 5

