from functools import reduce
count = int(input())
students = []
for i in range(count):
    lang_set = set()
    lang_count = int(input())
    for j in range(lang_count):
        lang_set.add(input())
    students.append(lang_set)

inter = reduce(lambda acc, s: acc.intersection(s), students, students[0])
union = reduce(lambda acc, s: acc.union(s), students, students[0])
print(len(inter))
print(*inter, sep='\n')
print(len(union))
print(*union, sep='\n')
