from collections import OrderedDict


def count_occurrences(string):
    unique_str = "".join(OrderedDict.fromkeys(string))
    new_str = ""
    for char in unique_str:
        # print(char)
        char_count = string.count(char)
        new_str = new_str + char
        new_str = new_str + '{}'.format(char_count)

    return new_str


input_str = 'occurrences'
print(count_occurrences(input_str))
