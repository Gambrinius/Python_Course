with open('input.txt', 'r', encoding='utf8') as input_file:
    lines = input_file.readlines()
    words_dict = dict()
    for line in lines:
        words = line.split()
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
    max_value = max(words_dict.values())
    keys_with_max_value = [key for key in words_dict 
						   if words_dict[key] == max_value]
    sorted_keys = sorted(keys_with_max_value)
    print(sorted_keys[0])
