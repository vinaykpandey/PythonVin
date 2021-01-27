'''

List comprehensions are used for creating new list from another iterables
As list comprehension returns list, they consists of brackets containing the
 expression which needs to be executed for each element along with the for loop
 to iterate over each element.

 new_list = [expression for_loop_one_or_more condtions]

'''


# Find squares of a number using for loop.

numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
  squares.append(n**2)

print(squares) # Output: [1, 4, 9, 16]

#Finding squares using list comprehensions

numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]

print(squares) # Output: [1, 4, 9, 16]