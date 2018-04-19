numList = list(map(int, input().split()))
k, C = tuple(map(int, input().split()))

numList.insert(k, C)
print(' '.join(map(str, numList)))
