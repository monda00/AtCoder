'''
[c - repsept](https://atcoder.jp/contests/abc174/tasks/abc174_c)
'''

k = int(input())

ans = -1
a = [7 % k]
for i in range(k):
    a.append((a[-1]*10+7) % k)

for i in range(k):
    if a[i] == 0:
        ans = i+1
        break

print(ans)
