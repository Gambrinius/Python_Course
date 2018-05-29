n = int(input())
cities_dict = dict()
for i in range(n):
    input_list = input().split()
    country = input_list[0]
    cities = input_list[1:]
    for city in cities:
        if city not in cities_dict:
            cities_dict[city] = country

k = int(input())
for _ in range(k):
    test_city = input()
    print(cities_dict[test_city])
