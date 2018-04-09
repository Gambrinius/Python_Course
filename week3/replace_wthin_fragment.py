string = input()

start = string.find('h')
end = string.rfind('h')
fragment = string[start + 1:end]

print(string[:start+1] + fragment.replace('h', 'H') + string[end:])
