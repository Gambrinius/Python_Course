input_file = open("input.txt", "r", encoding="utf8")
scores = [[], [], []]

for line in input_file:
    surname, name, class_, score = tuple(line.split())
    if class_ == '9':
        scores[0].append(int(score))
    if class_ == '10':
        scores[1].append(int(score))
    if class_ == '11':
        scores[2].append(int(score))
input_file.close()

for class_score in scores:
    print(max(class_score), end=' ')
