a = int(input())

start = 10 ** a - 1
stop = 10 ** (a - 1) - 1

for i in range(start, stop, -2):
    print(i, end=' ')
