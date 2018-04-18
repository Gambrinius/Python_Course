numList = list(map(int, input().split()))

max = numList[0]
max_index = 0
for i in range(1, len(numList)):
    n = numList[i]
    if n > max:
        max = n
        max_index = i
print(max, max_index)
