n = int(input())
a1 = 0
a2 = 1
i = 1
sum_ = 0

while a2 != n:
    if a2 > n:
        i = -1
        break
    sum_ = a1 + a2
    a1, a2 = a2, sum_
    i += 1
print(i)
