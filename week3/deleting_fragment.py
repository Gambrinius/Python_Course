s = input()

start = s.find('h')
end = s.rfind('h') + 1

print(s[:start] + s[end:])
