'''
[D - Derangement](https://atcoder.jp/contests/abc072/tasks/arc082_b)
'''

n = int(input())
p = list(map(int, input().split()))
p = list(map(lambda x: x - 1, p))

ans = 0

for i in range(n):
    if i == n-1 and i == p[i]:
        p[i], p[i - 1] = p[i - 1], p[i]
        ans += 1
    elif i == p[i]:
        p[i], p[i + 1] = p[i + 1], p[i]
        ans += 1

print(ans)
