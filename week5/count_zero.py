n = int(input())

counter = 0
for i in range(n):
    cur_num = int(input())
    if not cur_num:
        counter += 1
print(counter)
