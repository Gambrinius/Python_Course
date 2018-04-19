numList = list(map(int, input().split()))

i = 0
newList = []
while i < len(numList):
    if i + 1 == len(numList) and len(numList) % 2 != 0:
        newList.append(numList[i])
        break
    newList.append(numList[i+1])
    newList.append(numList[i])
    i += 2
print(*newList)
