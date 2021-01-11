'''
[C - 怪文書](https://atcoder.jp/contests/abc058/tasks/arc071_a)
'''

n = int(input())
S = list()
for _ in range(n):
    S.append(list(input()))

ans = list()
dup = S[0]
for i in range(1, n):
    s = S[i]
    de = list()
    for d in dup:
        if d in s:
            s.remove(d)
        else:
            de.append(d)
    for d in de:
        dup.remove(d)

dup.sort()
print(''.join(dup))
