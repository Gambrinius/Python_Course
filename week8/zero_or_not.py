print(
    any(
        map(
            lambda i: i == 0,
            map(
                lambda x: int(input().strip()),
                range(int(input()))
            )
        )
    )
)
