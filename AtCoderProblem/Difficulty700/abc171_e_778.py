'''
[E - Red Scarf](https://atcoder.jp/contests/abc171/tasks/abc171_e)
'''

n = int(input())
a = list(map(int, input().split()))

all_a = 0
for i in range(n):
    all_a ^= a[i]

ans = []
for i in range(n):
    ans.append(all_a ^ a[i])

print(*ans)
