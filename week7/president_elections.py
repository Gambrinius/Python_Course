candidates_set = set()
candidates_dict = dict()
with open('input.txt', 'r', encoding='utf8') as input_file:
    for line in input_file:
        candidate = line.strip()
        candidates_dict[candidate] = candidates_dict.get(candidate, 0) + 1
        candidates_set.add(candidate)

total_votes = sum(candidates_dict.values())
candidates_list = []
for candidate, votes in candidates_dict.items():
    candidates_list.append((votes / total_votes, candidate))
candidates_list.sort(reverse=True)
results = [candidate for candidate in candidates_list if candidate[0] > 0.5]

with open('output.txt', 'w', encoding='utf8') as output_file:
    if results:
        print(results[0][1], file=output_file)
    else:
        print(candidates_list[0][1], file=output_file)
        print(candidates_list[1][1], file=output_file)
