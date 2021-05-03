n = int(input())
s = list()
for i in range(n):
    s.append(list(input()))

for i in range(n):
    for j in range(n-1, -1, -1):
        print(s[j][i], end='')
    print()

