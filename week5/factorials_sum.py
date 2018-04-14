def factorial(num):
    if num != 0:
        return num * factorial(num - 1)
    return 1


n = int(input())
result = 0
for num in range(1, n + 1):
    result += factorial(num)
print(result)
