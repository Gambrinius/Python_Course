bank_customers = dict()
all_operations_set = {'DEPOSIT', 'WITHDRAW', 'BALANCE', 'TRANSFER', 'INCOME'}
client_operations_set = {'DEPOSIT', 'WITHDRAW', 'TRANSFER'}
with open('input.txt', 'r', encoding='utf8') as input_file:
    for line in input_file:
        line_list = line.split()
        operation = line_list[0]

        if operation in client_operations_set:
            if operation == 'DEPOSIT':
                name, amount = tuple(line_list[1:])
                bank_customers[name] = bank_customers.get(name, 0) \
                    + int(amount)
            if operation == 'WITHDRAW':
                name, amount = tuple(line_list[1:])
                bank_customers[name] = bank_customers.get(name, 0) \
                    - int(amount)
            if operation == 'TRANSFER':
                name1, name2, amount = tuple(line_list[1:])
                bank_customers[name1] = bank_customers.get(name1, 0) \
                    - int(amount)
                bank_customers[name2] = bank_customers.get(name2, 0) \
                    + int(amount)

        if operation == 'BALANCE':
            name = line_list[1]
            if name not in bank_customers:
                print('ERROR')
            else:
                print(int(bank_customers[name]))

        if operation == 'INCOME':
            percent = int(line_list[1])
            for client in bank_customers:
                client_amount = bank_customers[client]
                if client_amount > 0:
                    total_amount = int(client_amount * (100 + percent) // 100)
                    bank_customers[client] = total_amount
