with open('input.txt', 'r', encoding='utf8') as input_file:
    candidate_dict = dict()
    for line in input_file:
        candidate, votes = tuple(line.split())
        if candidate not in candidate_dict:
            candidate_dict[candidate] = int(votes)
        else:
            candidate_dict[candidate] += int(votes)

for candidate in sorted(candidate_dict):
    print(candidate, candidate_dict[candidate], sep=' ')
