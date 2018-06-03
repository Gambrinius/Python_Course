from functools import reduce
print(
    reduce(
        lambda acc, i: acc * i,
        map(
            lambda x: x ** 5,
            map(
                int,
                input().split()
            )
        )
    )
)
