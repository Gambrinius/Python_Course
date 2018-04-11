def fast_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_pow(a ** 2, n/2)
    else:
        return a * fast_pow(a, n-1)


a = float(input())
n = int(input())
print(fast_pow(a, n))
