'''
[D - Lucky PIN](https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d)
'''

n = int(input())
s = list(input())

ans = 0
for i in range(1000):
    key = str(i).zfill(3)
    key_i = 0
    for c in s:
        if c == key[key_i]:
            key_i += 1
        if key_i == 3:
            ans += 1
            break

print(ans)
