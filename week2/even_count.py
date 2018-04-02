num = int(input())

result_sum = 0
counter = 0
while num != 0:
    if num % 2 == 0:
        counter += 1
    num = int(input())
print(counter)
