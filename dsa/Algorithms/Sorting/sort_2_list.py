A = [30, 40, 10, 20, 50]
B = ['c','d','a','b','e']

for loopCount in range(len(A)-1):
    for i in range(len(A)-1-loopCount):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            B[i], B[i + 1] = B[i + 1], B[i]

print(A)
print(B)