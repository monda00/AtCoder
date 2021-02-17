'''
[B - Sum of Three Integers](https://atcoder.jp/contests/abc051/tasks/abc051_b)
'''

k, s = map(int, input().split())

ans = 0
for x in range(k+1):
    for y in range(k+1):
        z = s - x - y
        if z >= 0 and z <= k:
            ans += 1

print(ans)
