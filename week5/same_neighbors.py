numList = list(map(int, input().split()))

prev_num = 0
for num in numList:
    if (num < 0 and prev_num < 0) or (num > 0 and prev_num > 0):
        print(prev_num, num, sep=' ')
        break
    prev_num = num
