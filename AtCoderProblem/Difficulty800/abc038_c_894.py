'''
[C - 単調増加](https://atcoder.jp/contests/abc038/tasks/abc038_c)
'''

n = int(input())
A = list(map(int, input().split()))

inc = 1
ans = 1
for i in range(1, n):
    if A[i-1] < A[i]:
        inc += 1
        ans += inc
    else:
        inc = 1
        ans += inc

print(ans)
