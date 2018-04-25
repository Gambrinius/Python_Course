free_space, users_count = tuple(map(int, input().split()))

spaces_list = []
while users_count != 0:
    used_space = int(input())
    spaces_list.append(used_space)
    users_count -= 1

counter = 0
spaces_list.sort()
for space in spaces_list:
    if free_space - space >= 0:
        free_space -= space
        counter += 1

print(counter)
