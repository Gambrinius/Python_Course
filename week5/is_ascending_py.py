def IsAscending(A):
    index = 1
    while index < len(A) and A[index] > A[index - 1]:
        index += 1
    return "YES" if len(A) == index else "NO"


numList = list(map(int, input().split()))
print(IsAscending(numList))
