def all_sub_str(str):
    n = len(str)
    #start
    for i in range(1, n+1):
        #end point
        for j in range(n-i+1):
            k = j+i-1
            for l in range(j, k+1):
                print(str[l], end="")
            print()

# all_sub_str("abcd")

def  all_substr(str):
    n = len(str)
    for i in range(n):
        for j in range(i+1, n+1):
            print(str[i: j])

# all_substr("abc")

def all_sub(str):
    n = len(str)
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += str[j]
            print(temp)
all_sub("abc")