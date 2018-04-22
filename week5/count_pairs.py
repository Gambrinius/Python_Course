numList = list(map(int, input().split()))
# print(sum(numList.count(x) - 1 for x in numList) // 2)

counter = 0
for i in range(len(numList)):
    for j in range(i + 1, len(numList)):
        if numList[i] == numList[j]:
            counter += 1
print(counter)
