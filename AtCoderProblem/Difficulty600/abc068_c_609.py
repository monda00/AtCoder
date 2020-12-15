'''
[C - Cat Snuke and a Voyage](https://atcoder.jp/contests/abc068/tasks/arc079_a)
'''

n, m = map(int, input().split())
A = list()
B = list()
for _ in range(m):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

relay_from = list()
relay_to = list()

for i in range(m):
    if A[i] == 1:
        relay_from.append(B[i])
    if B[i] == n:
        relay_to.append(A[i])

if len(set(relay_from) & set(relay_to)) > 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
