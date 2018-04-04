price = float(input())

whole_part = int(price)
fract_part = round((price - whole_part) * 100)
print('{0} {1}'.format(whole_part, fract_part))
