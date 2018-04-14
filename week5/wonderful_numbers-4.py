a = int(input())
b = int(input())

for num in range(a, b + 1):
    if str(num)[:2] == str(num)[-1:-3:-1]:
        print(num)
