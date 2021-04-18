def count_substring(string, sub_string):
    count = 0
    i = 0
    while i < (len(string) - len(sub_string) + 1):
        print('step 1  i  == ', i)
        i = string.find(sub_string, i, len(string))
        print('step 2  i  == ', i)
        print('i==', i)
        if i != -1:
            count = count + 1
            i = i + 1
            print('count increment by 1 == ', count)
            print('i increment by 1 == ', i)
        elif i > 10:
            print('gt than 10')
            break
        else:
            print(i)
            break
    return count


string = 'ABCDCDC'
sub_string = 'CDC'
ret_count = count_substring(string, sub_string)
print('ret_count ==', ret_count)
