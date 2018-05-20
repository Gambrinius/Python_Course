n = int(input())
buttons_resistance = list(map(int, input().split()))
count_presses = int(input())
presses_list = list(map(int, input().split()))

for index in presses_list:
    buttons_resistance[index-1] -= 1

print(*["YES" if i < 0 else "NO" for i in buttons_resistance], sep='\n')
