def revert_sequence():
    n = int(input())

    if n != 0:
        revert_sequence()
        print(n)
    else:
        print(n)


revert_sequence()
