k = int(input())

if k % 3 == 0 or k % 5 == 0:
    print("YES")
else:
    balance = k % 5
    if balance % 3 == 0:
        print("YES")
    else:
        print("NO")
