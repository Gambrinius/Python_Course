# def intersection(a: list, b: list):
#     result_list = []
#     for num in a:
#         if num in b:
#             result_list.append(num)
#     return result_list


aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
# if len(aList) > len(bList):
#     aList, bList = bList, aList

# print(*intersection(aList, bList))
result_list = sorted(list(set(aList) & set(bList)))
print(*result_list)
