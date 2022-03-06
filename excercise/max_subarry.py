def longestSubarray(arr):
    # Write your code here
    sub_max = 0
    super_max = 0
    prev_elem = arr[0]
    two_distinct = set()
    l = 0
    for i in arr:
        l = l + 1
        print(l)
        print(i, prev_elem)
        print("two_distinct: ", two_distinct)
        if i == prev_elem:
            two_distinct.add(i)
            sub_max += 1

        elif len(two_distinct) <= 2:
            if abs(i - prev_elem) > 1:
                print(" >>> 2 diff ")
                if sub_max > super_max:
                    super_max = sub_max
                sub_max = 1
                two_distinct = set()
                two_distinct.add(i)
            elif len(two_distinct) < 2:
                if sub_max > super_max:
                    super_max = sub_max
                sub_max = 1
                two_distinct.add(i)
            else:
                print("sub_max::: ", sub_max)
                sub_max += 1

        prev_elem = i
    else:
        if sub_max > super_max:
            super_max = sub_max

    print(super_max)

    return super_max


a = [157793605, 157793605, 157793604, 157793604, 157793604, 157793604, 157793605, 157793605, 157793605, 157793604,
     157793605, 157793604, 157793605, 157793605, 157793604, 157793604, 157793604, 157793605, 157793605, 157793605,
     157793605, 157793604, 157793604, 157793605, 157793604, 157793605, 157793605, 157793605, 157793604, 157793605,
     157793605]

b = [1, 1, 1, 3, 3, 2, 2]

x = longestSubarray(a)

print("xxxx:: ", x)
