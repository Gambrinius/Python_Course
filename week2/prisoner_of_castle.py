a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

sum_ = a + b + c
max_elem = max(a, b, c)
min_elem = min(a, b, c)
mid_elem = sum_ - max_elem - min_elem
if d > e:
    d, e = e, d

if min_elem <= d and mid_elem <= e:
    print("YES")
else:
    print("NO")
