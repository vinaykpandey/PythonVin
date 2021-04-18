s = "aabbacccdccc"
list_a = []
list_a.append(s[0])
s2 = ""
for i in range(1, len(s)):
    char = s[i]
    if s[i] in list_a:
        list_a.append(char)
    else:
        length = len(list_a)
        last_ele = list_a[-1]
        s2 = "{}{}{}".format(s2, last_ele, length)
        list_a = []
        list_a.append(char)

print(s2)
