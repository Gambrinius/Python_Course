numList = list(map(int, input().split()))

max_num = numList[0]
max_count = numList.count(max_num)
for num in numList:
    if max_count < numList.count(num):
        max_num = num
        max_count = numList.count(num)
print(max_num)
