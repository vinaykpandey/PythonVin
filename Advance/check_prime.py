n = int(input("Enter number \n"))
for i in range(2, n):
    if n%i == 0:
        print("Prime Number")
        break;
else:
    print("Not a prime number")