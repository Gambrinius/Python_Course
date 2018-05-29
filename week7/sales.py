customers_dict = dict()
with open('input.txt', 'r', encoding='utf8') as input_file:
    for line in input_file:
        name, goods, count = tuple(line.split())
        if name not in customers_dict:
            customers_dict[name] = {goods: int(count)}
        else:
            if goods not in customers_dict[name]:
                customers_dict[name][goods] = int(count)
            else:
                customers_dict[name][goods] += int(count)

for customer in sorted(customers_dict):
    print('%s:' % customer)
    for good in sorted(customers_dict[customer]):
        print(good, customers_dict[customer][good], sep=' ')
