def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)


def ReduceFraction(n, m):
    gcd_result = gcd(n, m)
    # if n % 2 == 0 and m % 2 == 0:
    #     return ReduceFraction(n // 2, m // 2)
    # if m % n == 0 and n > 1:
    #     return ReduceFraction(n // n, m // n)
    return n // gcd_result, m // gcd_result


n = int(input())
m = int(input())
print('{0[0]} {0[1]}'.format(ReduceFraction(n, m)))
