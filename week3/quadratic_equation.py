a = float(input())
b = float(input())
c = float(input())

D = ((b**2) - (4 * a * c))
if D > 0:
    x1 = (-1 * b + D ** 0.5) / (2 * a)
    x2 = (-1 * b - D ** 0.5)/(2 * a)
    print(min(x1, x2), max(x1, x2))
elif D == 0:
    x1 = (-1) * b / (2 * a)
    print(x1)
elif D < 0:
    pass
elif c == 0:
    x2 = -b // a
    print(0, x2)
