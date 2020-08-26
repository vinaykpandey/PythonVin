def compute_lcm(x, y):
    min_v = min(x, y)
    max_v = max(x, y)
    print("max step 1", max_v)
    probable_lcm = max_v
    i = 0
    while (True):
        i = i + 1
        if probable_lcm % x == 0 and probable_lcm % y == 0:
            lcm_v = probable_lcm
            break
        probable_lcm += max_v
        print("max step 2", max_v)
    print("loop count is: ", i)
    return lcm_v


lcm_v = compute_lcm(10, 16)
print("lcm is: {0}".format(lcm_v))
