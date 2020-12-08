'''
[A - Prefix and Suffix](https://atcoder.jp/contests/agc006/tasks/agc006_a)
'''

n = int(input())
s = input()
t = input()

dup = 0
for i in range(n):
    if s[i:] == t[:(n-i)]:
        dup = n - i
        break

ans = dup + (n - dup)*2
print(ans)
