number = int(input())
inverse_num = 0

while number > 0:
    digit = number % 10
    number //= 10
    inverse_num *= 10
    inverse_num += digit
print(inverse_num)
