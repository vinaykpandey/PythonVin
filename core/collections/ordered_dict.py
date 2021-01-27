from collections import OrderedDict
def count_occurrences(str):
    uniqstr = "".join(OrderedDict.fromkeys(str))
    newstr = ""
    for char in uniqstr:
        # print(char)
        char_count = str.count(char)
        newstr = newstr + char
        newstr = newstr + '{}'.format(char_count)

    return newstr

str = 'occurrences'
print(count_occurrences(str))
