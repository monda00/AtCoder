'''
[B - さかさま辞書](https://atcoder.jp/contests/arc003/tasks/arc003_2)
'''

n = int(input())
S = []
for _ in range(n):
    s = list(input())
    s.reverse()
    S.append(s)

S.sort()

for i in range(len(S)):
    s = S[i]
    s.reverse()
    print(''.join(s))
