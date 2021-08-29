n = int(input())
name = []

for _ in range(n):
    s, t = input().split()
    name.append(s+' '+t)

name_set = set(name)

if len(name) == len(name_set):
    print('No')
else:
    print('Yes')
