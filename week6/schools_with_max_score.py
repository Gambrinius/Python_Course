input_file = open("input.txt", "r", encoding="utf8")
schools = [0] * 100

for line in input_file:
    surname, name, school_num, score = tuple(line.split())
    schools[int(school_num)] += 1
max_count = max(schools)
max_1 = schools.index(max_count)
try:
    max_2 = schools.index(max_count, max_1+1)
except ValueError:
    max_2 = -1

if max_2 != -1:
    print(max_1, max_2)
else:
    print(max_1)
input_file.close()
