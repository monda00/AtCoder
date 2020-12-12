'''
[C - Traveling Plan](https://atcoder.jp/contests/arc093/tasks/arc093_a)
'''

n = int(input())
a = list(map(int, input().split()))

fee_sum = abs(a[0])
for i in range(n):
    if i == n-1:
        fee_sum += abs(a[i]-0)
    else:
        fee_sum += abs(a[i]-a[i+1])

for i in range(n):
    if i == 0:
        print(fee_sum-abs(a[i])-abs(a[i]-a[i+1])+abs(a[i+1]))
    elif i == n-1:
        print(fee_sum-abs(a[i-1]-a[i])-abs(a[i])+abs(a[i-1]))
    else:
        print(fee_sum-abs(a[i-1]-a[i])-abs(a[i]-a[i+1])+abs(a[i-1]-a[i+1]))
