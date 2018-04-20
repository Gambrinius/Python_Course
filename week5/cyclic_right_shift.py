numList = list(map(int, input().split()))
# last element + slice from exist_list
result_list = numList[-1:] + numList[:len(numList) - 1]
print(*result_list)
