places = 450
parties = list()
total_votes = 0
with open('input.txt', 'r', encoding='utf8') as input_file:
    for line in input_file:
        str_list = line.strip().split()
        votes = int(str_list[-1])
        total_votes += votes
        name = ' '.join(str_list[:len(str_list) - 1])
        parties.append((name, votes))

quotient = total_votes / places
party_places = list()
remainders_list = list()
total_counted_places = 0
for index, party in enumerate(parties):
    counted_places = party[1] // quotient
    party_places.append(counted_places)
    remainders_list.append((party[1] % quotient, parties[index][1], index))
    remainders_list.sort(reverse=True)
    total_counted_places += counted_places

if total_counted_places < places:
    remaining_places = places - total_counted_places
    while remaining_places > 0:
        for element in remainders_list:
            party_places[element[2]] += 1
            remaining_places -= 1
            if remaining_places == 0:
                break

for index, party in enumerate(party_places):
    print(parties[index][0], int(party), sep=' ')
