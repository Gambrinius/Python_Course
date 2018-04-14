n = int(input())

sum_ = sum(range(n+1))
for i in range(1, n):
    cur_num = int(input())
    sum_ -= cur_num
print(sum_)
