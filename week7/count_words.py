with open('input.txt', 'r', encoding='utf8') as input_file:
    count = {}
    for line in input_file:
        words = list(line.strip().split())
        for word in words:
            count[word] = count.get(word, 0) + 1
            print(int(count[word] - 1), end=' ')
