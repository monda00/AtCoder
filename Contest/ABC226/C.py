import sys
sys.setrecursionlimit(10**7)

n = int(input())
T = []
K = []
A = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    T.append(tmp[0])
    K.append(tmp[1])
    A.append([i-1 for i in tmp[2:]])

tech_set = set()
tech_set.add(n-1)


def dfs(x):
    if x in tech_set:
        return

    tech_set.add(x)

    for a in A[x]:
        dfs(a)


for a in A[-1]:
    dfs(a)

ans = 0

for s in tech_set:
    ans += T[s]

print(ans)
