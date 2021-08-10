'''
https://atcoder.jp/contests/agc013/tasks/agc013_a
'''

n = int(input())
A = list(map(int, input().split()))

ans = 1
pre = A[0]
monotonic = 'neural'

for i in range(1, n):
    if monotonic == 'neural' and pre < A[i]:
        monotonic = 'increase'
    elif monotonic == 'neural' and pre > A[i]:
        monotonic = 'decrease'
    elif monotonic == 'increase' and pre > A[i]:
        monotonic = 'neural'
        ans += 1
    elif monotonic == 'decrease' and pre < A[i]:
        monotonic = 'neural'
        ans += 1

    pre = A[i]

print(ans)
