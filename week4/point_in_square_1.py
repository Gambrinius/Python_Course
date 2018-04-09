def IsPointInSquare(x, y):
    if abs(x) <= 1 and abs(y) <= 1:
        return True
    return False


x = float(input())
y = float(input())

if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
