percents = int(input())
rub = int(input())
kop = int(input())

total = rub * 100 + kop
result_sum = total + (total * percents / 100)
result_rub = int(result_sum // 100)
result_kop = int(result_sum % 100)

print(result_rub, result_kop)
