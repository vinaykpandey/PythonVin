def sum_using_loop(n):
    AddNum = 0;
    #j = 0
    for i in range(n, 0, -1):
        #j = j+1
        #print(j)
        print('==n ===', n , ' ,,iiii ==', i);
        AddNum = AddNum+i
    return AddNum;
N = int(input("Input Number to add: "))
S = sum_using_loop(N)
print("Sum ===" , S);

