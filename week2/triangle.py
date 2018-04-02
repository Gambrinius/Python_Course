a = int(input())
b = int(input())
c = int(input())

max_elem = max(a, b, c)
min_elem = min(a, b, c)
mid_elem = sum([a, b, c]) - max_elem - min_elem

if max_elem < mid_elem + min_elem:
    if max_elem ** 2 == mid_elem ** 2 + min_elem ** 2:
        print("rectangular")
    elif max_elem ** 2 < mid_elem ** 2 + min_elem ** 2:
        print("acute")
    elif max_elem ** 2 > mid_elem ** 2 + min_elem ** 2:
        print("obtuse")
else:
    print("impossible")
