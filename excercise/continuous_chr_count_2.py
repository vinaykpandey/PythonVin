s = "aaabbaabbbccd"


def get_char_count(s):
    count = 0
    pivot = s[0]  # 1st time
    new_str = ""
    previous_char = None
    for c in s:
        if c == pivot:
            count = count + 1
        else:
            pivot = c
            new_str = "{}{}{}".format(new_str, previous_char, count)
            count = 1
        previous_char = c
    else:
        new_str = "{}{}{}".format(new_str, previous_char, count)

    return new_str


print(get_char_count(s))
