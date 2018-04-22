numList = list(map(int, input().split()))

# offset = 0
# for i in range(len(numList)):
#     j = i - offset
#     if numList[j] == 0:
#         numList.append(numList.pop(j))
#         offset += 1

zeroIndex = 999
for i in range(len(numList)):
    if numList[i] == 0:
        if i < zeroIndex:
            zeroIndex = i
    elif i > zeroIndex:
        numList[zeroIndex] = numList[i]
        numList[i] = 0
        zeroIndex += 1
print(*numList)
