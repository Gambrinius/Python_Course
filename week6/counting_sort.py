input_list = list(map(int, input().split()))
counting_list = [0] * 101
for elem in input_list:
    counting_list[elem] += 1

for index, count in enumerate(counting_list):
    print((str(index) + ' ') * count, end='')
