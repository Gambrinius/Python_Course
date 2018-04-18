numList = list(map(int, input().split()))

max_element = 0
max_index = 0
for index, num in enumerate(numList):
    if num >= max_element:
        max_element = num
        max_index = index
print(max_element, max_index)
