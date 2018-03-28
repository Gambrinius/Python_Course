start_num = int(input())
last_num = int(input())

if last_num % (last_num - start_num + 1) == 0:
    print("YES")
else:
    print("NO")
