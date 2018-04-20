numList = list(map(int, input().split()))

if len(numList) == 3:
    print(*numList)
else:
    max1 = numList[0]
    min1 = numList[0]

    for n in numList:
        if n > max1:
            max1 = n
        if n < min1:
            min1 = n

    numList.remove(max1)
    numList.remove(min1)
    max2 = numList[0]
    min2 = numList[0]

    for n in numList:
        if n > max2:
            max2 = n
        if n < min2:
            min2 = n

    numList.remove(max2)

    max3 = numList[0]

    for n in numList:
        if n > max3:
            max3 = n

    multiply1 = min1 * min2 * max1
    multiply2 = max1 * max2 * max3

    if multiply1 > multiply2:
        print(min1, min2, max1)
    else:
        print(max1, max2, max3)
