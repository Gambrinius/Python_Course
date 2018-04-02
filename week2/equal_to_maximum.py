num = 1
max_num = -1
counter = 1
while num != 0:
    num = int(input())
    if num > max_num:
        max_num = num
        counter = 1
    elif num == max_num:
        counter += 1
print(counter)
