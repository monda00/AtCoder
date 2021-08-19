'''
[D - Number of Shortest paths](https://atcoder.jp/contests/abc211/tasks/abc211_d)
'''

from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

que = deque([0])
dist = [None] * n
cnt = [0] * n
dist[0] = 0
cnt[0] = 1

while que:
    v = que.popleft()
    for vv in G[v]:
        if dist[vv] is None:
            dist[vv] = dist[v] + 1
            que.append(vv)
            cnt[vv] = cnt[v]
        elif dist[vv] == dist[v] + 1:
            cnt[vv] += cnt[v]
            cnt[vv] %= 10**9+7

print(cnt[n-1])
