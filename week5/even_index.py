numList = list(map(int, input().split()))

for index in range(len(numList)):
    if index % 2 == 0:
        print(numList[index], end=' ')
