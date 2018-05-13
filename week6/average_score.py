input_file = open('input.txt', 'r', encoding='utf-8')

ninth_grade = 0
count_nine = 0
tenth_grade = 0
count_ten = 0
eleventh_grade = 0
count_eleven = 0
for line in input_file:
    surname, name, grade, score = tuple(line.split())
    if grade == '9':
        ninth_grade += int(score)
        count_nine += 1
    if grade == '10':
        tenth_grade += int(score)
        count_ten += 1
    if grade == '11':
        eleventh_grade += int(score)
        count_eleven += 1
print(ninth_grade/count_nine, tenth_grade/count_ten,
      eleventh_grade/count_eleven)
