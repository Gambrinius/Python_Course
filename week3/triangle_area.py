import math

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("{0:.10f}".format(S))
