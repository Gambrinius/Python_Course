numList = list(map(int, input().split()))


min_num = min(numList)
min_index = numList.index(min_num)
max_num = max(numList)
max_index = numList.index(max_num)

newList = numList.copy()
newList[min_index] = max_num
newList[max_index] = min_num
print(*newList)
