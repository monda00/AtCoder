'''
[C - HSI](https://atcoder.jp/contests/abc078/tasks/arc085_a)
'''

n, m = map(int, input().split())

ans = (1900 * m + 100*(n - m)) * (2**m)

print(ans)
