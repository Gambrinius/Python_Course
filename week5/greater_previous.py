numList = list(map(int, input().split()))

previous_element = numList[0]
for num in numList:
    if num > previous_element:
        print(num, end=' ')
    previous_element = num
