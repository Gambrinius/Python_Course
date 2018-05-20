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

max_nine = max(scores[0])
max_ten = max(scores[1])
max_eleven = max(scores[2])
print(scores[0].count(max_nine),
      scores[1].count(max_ten),
      scores[2].count(max_eleven), sep=' ')
