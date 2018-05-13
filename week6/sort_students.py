input_file = open('input.txt', 'r', encoding='utf-8')
student_list = []

for line in input_file:
    surname, name, school, score = line.split()
    student_list.append([surname, name, score])

student_list.sort(key=lambda s: s[0])
input_file.close()

with open('output.txt', 'w', encoding='utf-8') as output_file:
    for student in student_list:
        print(*student, file=output_file)
