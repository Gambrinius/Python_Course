n = int(input())
i = 1
sum_ = 0

while i <= n:
    sum_ += 1 / (i ** 2)
    i += 1

print("{0:.10f}".format(sum_))
