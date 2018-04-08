string = input()

first_entry = string.find('f')
second_entry = string.find('f', first_entry + 1)

if first_entry != -1:
    if second_entry != -1:
        print(second_entry)
    else:
        print(-1)
else:
    print(-2)
