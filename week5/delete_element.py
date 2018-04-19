numList = list(map(int, input().split()))
k = int(input())

numList.pop(k)
print(' '.join(map(str, numList)))
