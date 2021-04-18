def all_sub_str(param_str):
    n = len(param_str)
    # start
    for i in range(1, n + 1):
        # end point
        for j in range(n - i + 1):
            k = j + i - 1
            for l in range(j, k + 1):
                print(param_str[l], end="")
            print()


# all_sub_str("abcd")

def all_substr(param_str):
    n = len(param_str)
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(param_str[i: j])


# all_substr("abc")

def all_sub(param_str):
    n = len(param_str)
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += param_str[j]
            print(temp)


all_sub("abc")
