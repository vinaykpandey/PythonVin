''' only for loop & while loop exist in python
 do while not exist in python
 '''
primes = [2, 3, 5, 7]
# Prints out 2, 3, 5, 7
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4     < 5   always less than, never less than equal
for x in range(5):
    print(x)


# Prints out 3,4,5       < 6  always less than, never less than equal

for x in range(3, 6):
     print('increment by 1: ', x)


# Prints out 3,5,7    <  8
for x in range(3, 8, 2):
    print('increment by 2: ', x)
