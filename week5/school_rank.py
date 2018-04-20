pupilList = list(map(int, input().split()))
petya = int(input())

i = 0
position = 0
while i < len(pupilList):
    if pupilList[i] >= petya:
        position = i + 1
        i += 1
    else:
        break
print(position + 1)
