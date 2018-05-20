with open("input.txt", "r", encoding="utf8") as input_file:
    lines = list(map(lambda s: s.strip(), input_file.readlines()))

votes_index = lines.index('VOTES:')
parties = lines[1:votes_index]
votes = lines[votes_index + 1:]

votes_counter = [0] * len(parties)

for vote in votes:
    party_index = parties.index(vote)
    votes_counter[party_index] += 1
parties_votes = [(parties[index], vote)
                 for index, vote in enumerate(votes_counter)]

parties_votes.sort(key=lambda party: (-party[1], party[0]))

print(*[party[0] for party in parties_votes], sep='\n')
