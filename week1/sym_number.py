number = int(input())
k1 = 1
k2 = 2
k3 = 3

n3 = (number // 10 ** k1) % 10
n2 = (number // 10 ** k2) % 10
n1 = (number // 10 ** k3) % 10
n4 = (number % 10 ** k1)

print(n1 == n4 and n2 == n3 and 1 or 2)
