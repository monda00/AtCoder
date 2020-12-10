'''
[C - pushpush](https://atcoder.jp/contests/abc066/tasks/arc077_a)
'''

n = int(input())
a = list(map(int, input().split()))

odd = list()
even = list()
for i in range(n):
    if i % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

odd.reverse()
ans = odd + even
if n % 2 == 1:
    ans.reverse()

print(*ans)
