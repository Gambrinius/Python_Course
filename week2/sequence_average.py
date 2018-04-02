num = int(input())

result_sum = 0
counter = 0
while num != 0:
    result_sum += num
    counter += 1
    num = int(input())
print(result_sum / counter)
