'''
[B - Choose Integers](https://atcoder.jp/contests/abc060/tasks/abc060_b)
'''

a, b, c = map(int, input().split())

for i in range(b):
    if (i * a) % b == c:
        print('YES')
        exit()

print('NO')
