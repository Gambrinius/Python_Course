numList = list(map(int, input().split()))

for num in numList:
    if numList.count(num) == 1:
        print(num, end=' ')
