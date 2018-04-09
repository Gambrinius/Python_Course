def xor(x, y):
    return not (x == y)


x = int(input())
y = int(input())
if xor(x, y):
    print(1)
else:
    print(0)
