'''
[B - Uniformly Distributed](https://atcoder.jp/contests/arc120/tasks/arc120_b)
'''

h, w = map(int, input().split())
S = []
for _ in range(h):
    S.append(list(input()))


set_ij = [set() for i in range(h+w)]

for i in range(h):
    for j in range(w):
        set_ij[i+j].add(S[i][j])

ans = 1
for s in set_ij:
    if len(s) == 1 and "." in s:
        ans *= 2
        ans %= 998244353
    elif "R" in s and "B" in s:
        ans *= 0

print(ans)
