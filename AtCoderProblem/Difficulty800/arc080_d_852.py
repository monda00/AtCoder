'''
[D - Grid Coloring](https: // atcoder.jp/contests/arc080/tasks/arc080_b)
'''

h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
A = dict()
for a_i in range(len(a)):
    A[str(a_i)] = a[a_i]
A = sorted(A.items(), key=lambda x: x[1], reverse=True)

ans = [[0 for _ in range(w)] for _ in range(h)]

a_i = 0
now = A[a_i][1]
plus = True
for i in range(h):
    if plus:
        for j in range(w):
            now -= 1
            ans[i][j] = int(A[a_i][0]) + 1
            if now == 0:
                a_i += 1
                if a_i < n:
                    now = A[a_i][1]
    else:
        for j in range(w-1, -1, -1):
            now -= 1
            ans[i][j] = int(A[a_i][0]) + 1
            if now == 0:
                a_i += 1
                if a_i < n:
                    now = A[a_i][1]
    plus = not plus

for an in ans:
    print(*an)
