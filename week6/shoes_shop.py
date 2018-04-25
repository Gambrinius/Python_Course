foot_size = int(input())
sizeList = list(map(int, input().split()))
sizeList.sort()

counter = 0
current_size = 0
for size in sizeList:
    if size < foot_size:
        continue
    elif size == current_size:
        continue
    elif size == foot_size:
        counter += 1
        current_size = size
    elif size - current_size >= 3:
        counter += 1
        current_size = size
print(counter)
