'''
[C - ORXOR](https://atcoder.jp/contests/abc197/tasks/abc197_c)
'''

n = int(input())
A = list(map(int, input().split()))

ans = 2**30

# 区切る箇所をビット探索で
for i in range(2**(n-1)):
    or_ = 0
    xor = 0
    for j in range(n):
        or_ |= A[j]
        # 区切る箇所がきたら
        if (i >> j) & 1:
            xor ^= or_
            or_ = 0
    xor ^= or_
    ans = min(ans, xor)

print(ans)
