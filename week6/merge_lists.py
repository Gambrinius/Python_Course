def merge(a: list, b: list):
    result_list = a + b
    j = 0   # index for list A
    i = 0   # index for list B
    for k in range(len(result_list)):
        if i > len(a) - 1:  # add remaining nums from B
            result_list[k] = b[j]
            j += 1
        elif j > len(b) - 1:  # add remaining nums from A
            result_list[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            result_list[k] = a[i]
            i += 1
        else:
            result_list[k] = b[j]
            j += 1
    return result_list


aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
print(*merge(aList, bList))
