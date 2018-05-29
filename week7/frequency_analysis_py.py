def sort_alphabetic(tup):
    return -tup[0], tup[1]


with open('input.txt', 'r', encoding='utf8') as input_file:
    lines = input_file.readlines()
    words_dict = dict()
    for line in lines:
        words = line.split()
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

    words_list = []
    for key, values in words_dict.items():
        words_list.append((values, key))

    words_list.sort(key=sort_alphabetic)
    print(*[word[1] for word in words_list], sep='\n')