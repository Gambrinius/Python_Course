from functools import reduce

print(
    *map(
        lambda tup: reduce(lambda acc, x: acc ^ x, tup),
        zip(*list(
                  map(
                      lambda x: map(int, input().split()),
                      range(int(input()))
                     )
                 )
            )
    )
)
