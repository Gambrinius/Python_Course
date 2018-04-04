num = int(input())
prev = -1
curr_count = 0
max_count = 0

while num != 0:
    if num == prev:
        curr_count += 1
    else:
        prev = num
        max_count = max(max_count, curr_count)
        curr_count = 1
    num = int(input())

max_count = max(max_count, curr_count)
print(max_count)
