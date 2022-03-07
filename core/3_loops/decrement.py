def sum_using_loop(n):
    counter = 0
    # j = 0
    for i in range(n, 0, -1):
        # j = j+1
        # print(j)
        print(f'==n ==={n},  i== {i}')
        counter = counter + i
    return counter


n = int(input("Input Number to add: "))
s = sum_using_loop(n)
print(f"Sum ===, {s}")

