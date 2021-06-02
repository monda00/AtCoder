'''
[C - ORXOR](https://atcoder.jp/contests/abc197/tasks/abc197_c)
'''

n = int(input())
A = list(map(int, input().split()))

ans = 1 << 30

for i in range(1 << (n-1)):
    or_ = 0
    xor = 0
    for j in range(len(A)):
        or_ |= A[j]
        if j + 1 == len(A):
            xor ^= or_
            continue
        if (i >> j) & 1:
            xor ^= or_
            or_ = 0
    ans = min(ans, xor)

print(ans)
