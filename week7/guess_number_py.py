with open('input.txt', 'r', encoding='utf-8') as input_file:
    n = int(input_file.readline())
    right = set(range(1, n + 1))
    for line in input_file:
        if "YES" in line:
            right &= temp
        elif "NO" in line:
            right -= temp
        elif "HELP" not in line:
            temp = set(map(int, line.split()))
    print(' '.join(map(str, sorted(right))))
