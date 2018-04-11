def power(a, n):
    sum = 1
    if n == 0:
        return 1
    if n < 0:
        while n != 0:
            sum *= 1 / a
            n += 1
        return sum
    if n > 0:
        while n != 0:
            sum *= a
            n -= 1
        return sum


a = float(input())
n = int(input())
print(power(a, n))
