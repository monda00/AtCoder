'''
[C - Switches](https://atcoder.jp/contests/abc128/tasks/abc128_c)
'''

n, m = map(int, input().split())
k = []
s = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    k.append(tmp[0])
    s.append(tmp[1:])

p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    switch = [0] * n
    for j in range(n):
        if(i >> j) & 1:
            switch[j] = 1
    for j in range(m):
        k_sum = 0
        for s_i in range(k[j]):
            k_sum += switch[s[j][s_i]-1]
        if k_sum % 2 != p[j]:
            break
        if j == m-1:
            ans += 1

print(ans)
