numList = list(map(int, input().split()))

min_element = 1000
for index, num in enumerate(numList):
    if min_element > num > 0:
        min_element = num
print(min_element)
