'''
[A - Multiple Array](https://atcoder.jp/contests/agc009/tasks/agc009_a)
'''

n = int(input())
A = []
B = []
diff = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
for i in range(n-1, -1, -1):
    A[i] += ans
    if A[i] % B[i] == 0:
        ans += 0
    elif A[i] < B[i]:
        ans += B[i] - A[i]
    elif A[i] > B[i]:
        ans += (B[i]-(A[i] % B[i]))

print(ans)
