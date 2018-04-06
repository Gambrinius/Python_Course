percents = int(input())
rub = int(input())
kop = int(input())
duration = int(input())
current_year = 1

while current_year <= duration:
    total_kop = rub * 100 + kop
    result_sum = total_kop + (total_kop * percents / 100)
    rub = int(result_sum // 100)
    kop = int(result_sum % 100)
    current_year += 1

print(rub, kop)
