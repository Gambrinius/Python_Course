prev = int(input())
number = int(input())
max_count = 1
curr_count = 1

while True:
    if number == 0 or prev == 0:
        break

    while prev > number:
        if number == 0:
            break

        curr_count += 1
        if curr_count > max_count:
            max_count = curr_count

        prev = number
        number = int(input())

    curr_count = 1
    while prev < number:
        if number == 0:
            break

        curr_count += 1
        if curr_count > max_count:
            max_count = curr_count

        prev = number
        number = int(input())

    curr_count = 1
    while prev == number:
        prev = number
        number = int(input())
print(max_count)
