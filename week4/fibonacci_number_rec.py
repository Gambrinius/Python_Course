def phib(n, i=0, a=0, b=1):
    while n != i:
        return phib(n, i + 1, b, a + b)
    return a


n = int(input())
print(phib(n))
