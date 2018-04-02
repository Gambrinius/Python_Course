curr_num = int(input())
max_num = curr_num

while curr_num != 0:
    curr_num = int(input())
    if curr_num != 0 and max_num < curr_num:
        max_num = curr_num
print(max_num)
