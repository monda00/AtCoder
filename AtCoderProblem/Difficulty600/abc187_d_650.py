'''
[D - Choose Me](https://atcoder.jp/contests/abc187/tasks/abc187_d)
'''

n = int(input())
AB = []
all = 0
sum_a = 0
sum_b = 0
for _ in range(n):
    a, b = map(int, input().split())
    AB.append([a, b])
    all += a + b
    sum_a += a
    sum_b += b

AB = sorted(AB, key=lambda x: (2*x[0]+x[1]), reverse=True)

slip = 0
ans = 0
for (a, b) in AB:
    slip += (a + b)
    sum_a -= a
    ans += 1
    if slip > sum_a:
        print(ans)
        exit()
