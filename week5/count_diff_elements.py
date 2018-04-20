numList = list(map(int, input().split()))

counter = 1
prev_num = numList[0]
for num in numList:
    if prev_num != num:
        counter += 1
    prev_num = num
print(counter)
