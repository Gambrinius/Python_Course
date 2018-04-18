numList = list(map(int, input().split()))

even_list = [num for num in numList if num % 2 != 0]
print(min(even_list) if even_list else 0)
