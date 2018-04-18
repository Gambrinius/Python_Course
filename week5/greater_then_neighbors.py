numList = list(map(int, input().split()))

i = 1
counter = 0
while i < len(numList) - 1:
    if numList[i - 1] < numList[i] and numList[i] > numList[i + 1]:
        counter += 1
    i += 1
print(counter)
