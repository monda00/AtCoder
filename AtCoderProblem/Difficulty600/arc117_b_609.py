'''
[B - ARC Wrecker](https://atcoder.jp/contests/arc117/tasks/arc117_b)
'''

n = int(input())
A = list(map(int, input().split()))
A.sort()

Q = [A[0]]
for i in range(1, n):
    Q.append(A[i] - A[i - 1])

ans = 1
for i in range(n):
    ans *= (Q[i]+1)
    ans %= (10**9+7)

print(ans)
