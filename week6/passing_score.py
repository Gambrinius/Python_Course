input_file = open("input.txt", "r", encoding="utf8")
students_count = int(input_file.readline())
students = []

for line in input_file:
    elements = line.split()
    score1 = int(elements[-1])
    score2 = int(elements[-2])
    score3 = int(elements[-3])
    if score1 >= 40 and score2 >= 40 \
            and score3 >= 40:
        students.append([score1, score2, score3])
input_file.close()

students.sort(key=lambda s: s[0] + s[1] + s[2], reverse=True)

results = []
for student in students:
    results.append(sum(student))
results_count = len(results)


def competitions(results_count, students_count, results):
    if results_count <= students_count:
        return 0
    elif results[students_count] == results[0]:
        return 1
    for i in range(students_count, 0, -1):
        if results[i] < results[i - 1]:
            return results[i - 1]


with open("output.txt", "w", encoding="utf8") as output_file:
    output_file.write(
        str(competitions(results_count, students_count, results))
    )
