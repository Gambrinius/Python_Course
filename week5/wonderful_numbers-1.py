from functools import reduce

for num in range(10, 100):
    if num == 2 * reduce(lambda x, y: x*y, [int(digit) for digit in str(num)]):
        print(num)
