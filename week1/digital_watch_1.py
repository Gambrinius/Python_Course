minutes_time = int(input())
hours_time = minutes_time // 60 % 24
minutes_remainder = minutes_time % 60
print(hours_time, minutes_remainder)
