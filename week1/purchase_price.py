rubels = int(input())
coins = int(input())
quantity = int(input())

total_coins = (rubels * 100 + coins) * quantity
print(total_coins // 100, total_coins % 100)
