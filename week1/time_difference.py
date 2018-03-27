hours1 = int(input())
minutes1 = int(input())
seconds1 = int(input())

hours2 = int(input())
minutes2 = int(input())
seconds2 = int(input())

total_sec1 = hours1 * 3600 + minutes1 * 60 + seconds1
total_sec2 = hours2 * 3600 + minutes2 * 60 + seconds2
print(total_sec2 - total_sec1)
