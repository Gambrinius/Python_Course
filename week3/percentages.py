months = int(input())
roubles = int(input())
kopec = int(input())

whole_sum = roubles + kopec / 100
sum_ = whole_sum * (1 + months / 100)

whole_part = int(sum_)
fract_part = int((sum_ - whole_part) * 100)
print('{0} {1}'.format(whole_part, fract_part))
