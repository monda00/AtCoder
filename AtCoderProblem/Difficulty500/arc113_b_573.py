'''
[B - A^B^C](https://atcoder.jp/contests/arc113/tasks/arc113_b)
'''

a, b, c = map(int, input().split())

ans = pow(a, pow(b, c, 4)+4, 10)

print(ans)
