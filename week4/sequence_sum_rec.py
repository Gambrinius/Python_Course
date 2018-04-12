def sequence_sum():
    n = int(input())
    if n != 0:
        return n + sequence_sum()
    return 0


print(sequence_sum())
