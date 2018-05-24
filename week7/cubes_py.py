ann, boris = tuple(map(int, input().split()))
a = set()
b = set()
for i in range(ann):
    a.add(int(input()))
for i in range(boris):
    b.add(int(input()))

s_list = [sorted(a.intersection(b)), sorted(a.difference(b)),
          sorted(b.difference(a))]
for s in s_list:
    print(len(s))
    print(' '.join(map(str, s)))
