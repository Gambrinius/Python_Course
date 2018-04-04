number = float(input())

whole_part = int(number)
fract_part = number - whole_part

if fract_part >= 0.5:
    print(whole_part + 1)
else:
    print(whole_part)
