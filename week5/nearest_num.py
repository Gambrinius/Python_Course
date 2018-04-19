n = int(input())
numList = list(map(int, input().split()))
x = int(input())

if numList.count(x) > 0:
    print(x)
else:
    b = []
    for i in range(n):
        b.append(abs(numList[i] - x))
    index = b.index(min(b))
    print(numList[index])
