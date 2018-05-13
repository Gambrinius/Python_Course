N = int(input())
student_list = []
for i in range(N):
    surname, grade = tuple(input().split())
    student_list.append([surname, int(grade)])
student_list.sort(key=lambda s: s[1], reverse=True)

for student in student_list:
    print(student[0])
