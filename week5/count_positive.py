numList = list(map(int, input().split()))

counter = 0
for num in numList:
    if num > 0:
        counter += 1
print(counter)
