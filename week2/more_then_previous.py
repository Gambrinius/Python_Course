num = int(input())

prev = num
counter = 0

while num != 0:
    num = int(input())
    if num > prev:
        counter += 1
    prev = num
print(counter)
