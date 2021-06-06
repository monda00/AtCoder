import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
A = []
B = []
for _ in range(m):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)

route = [[] for _ in range(n)]

for i in range(m):
    route[A[i]].append(B[i])


def dfs(v):
    if check[v]:
        return
    check[v] = True
    for vv in route[v]:
        dfs(vv)


ans = 0
for i in range(n):
    check = [False] * n
    dfs(i)
    ans += sum(check)

print(ans)
