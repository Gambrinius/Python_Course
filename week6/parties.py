with open("input.txt", "r", encoding="utf8") as input_file:
    lines = list(map(lambda s: s.strip(), input_file.readlines()))

votes_index = lines.index('VOTES:')
parties = lines[1:votes_index]
votes = lines[votes_index + 1:]

votes_counter = [0] * len(parties)

for vote in votes:
    party_index = parties.index(vote)
    votes_counter[party_index] += 1

total_votes_count = sum(votes_counter)
votes_counter = map(lambda x: x/total_votes_count * 100, votes_counter)

for index, counter in enumerate(votes_counter):
    if counter >= 7:
        print(parties[index])
