total_seconds = int(input())

hours = total_seconds // 3600 % 24
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 3600 % 60

print('{0}:{1:02d}:{2:02d}'.format(hours, minutes, seconds))
