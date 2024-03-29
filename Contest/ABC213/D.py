import sys
sys.setrecursionlimit(300000)

n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(n+1):
    G[i].sort()

ans = []


def dfs(crr, pre):
    ans.append(crr)
    for nxt in G[crr]:
        if nxt != pre:
            dfs(nxt, crr)
            ans.append(crr)


dfs(1, -1)
print(*ans)
