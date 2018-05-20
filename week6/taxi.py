from functools import reduce

distances = sorted(list(map(int, input().split())))
prices = sorted(list(map(int, input().split())), reverse=True)
pairs = zip(distances, prices)
print(reduce(lambda acc, x: acc + x[0] * x[1], pairs, 0))
