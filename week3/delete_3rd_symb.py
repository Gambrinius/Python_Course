string = input()

i = 0
result = ''
while i != len(string):
    if i % 3 == 0:
        i += 1
        continue
    result += string[i]
    i += 1
print(result)
