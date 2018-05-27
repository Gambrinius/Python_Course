def reformat(string):
    string = string.replace('-', '').replace('(', '').replace(')', '')

    return string[-10:] if len(string) > 7 else '495' + string[-7:]


n = 4
phones = [input() for _ in range(n)]
for phone in phones[1:]:
    print('YES' if reformat(phones[0]) == reformat(phone) else 'NO')
