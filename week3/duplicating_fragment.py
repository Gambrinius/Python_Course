s = input()

start = s.find('h')
end = s.rfind('h')
fragment = s[start + 1: end]

print(s[:end] + fragment + s[end:])
