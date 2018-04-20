numList = list(map(int, input().split()))

max1 = numList[0]
min1 = numList[0]
for current_num in numList:
    if current_num > max1:
        max1 = current_num
    if current_num < min1:
        min1 = current_num
numList.remove(max1)
numList.remove(min1)

max2 = numList[0]
min2 = numList[0]
for current_num in numList:
    if current_num > max2:
        max2 = current_num
    if current_num < min2:
        min2 = current_num

if min1 * min2 > max1 * max2:
    print(min1, min2)
else:
    print(max2, max1)
