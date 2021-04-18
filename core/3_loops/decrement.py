def sum_using_loop(n):
    add_num = 0
    # j = 0
    for i in range(n, 0, -1):
        # j = j+1
        # print(j)
        print('==n ===', n, ' ,,iiii ==', i)
        add_num = add_num + i
    return add_num


n = int(input("Input Number to add: "))
s = sum_using_loop(n)
print("Sum ===", s)
