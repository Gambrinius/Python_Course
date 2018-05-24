numbers_list = list(map(int, input().split()))
numbers_set = set()
for number in numbers_list:
    if number in numbers_set:
        print("YES")
    else:
        numbers_set.add(number)
        print("NO")
