# Python3 implementation of recursive
# approach to find the number of set
# bits in binary representation of
# positive integer n

def countSetBits(n):
    print('nn=== ', n)
    # base case
    if (n == 0):
        return 0

    else:
        # if last bit set add 1 else
        # add 0
        return (n & 1) + countSetBits(n/2)    # countSetBits(n >> 1)


# Get value from user
n = 10
print((n & 1))
print(n >> 1)
# Function calling
print(countSetBits(n))

# This code is contributed by