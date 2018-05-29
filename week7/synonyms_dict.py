n = int(input())
synonyms_dict = dict()
for i in range(n):
    word1, word2 = tuple(input().split())
    synonyms_dict[word1] = word2
    synonyms_dict[word2] = word1
test_word = input()
print(synonyms_dict[test_word])
