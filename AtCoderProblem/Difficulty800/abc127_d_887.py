'''
[D - Integer Cards](https://atcoder.jp/contests/abc127/tasks/abc127_d)
'''

n, m = map(int, input().split())
A = list(map(int, input().split()))
BC = []
for _ in range(m):
    BC.append(list(map(int, input().split())))

A.sort()
BC.sort(key=lambda x: x[1])

ans = sum(A)
for i in range(n):
    if BC[-1][0] == 0:
        BC.pop()
    if not BC:
        break
    if A[i] > BC[-1][1]:
        break
    else:
        ans += BC[-1][1] - A[i]
        BC[-1][0] -= 1

print(ans)
