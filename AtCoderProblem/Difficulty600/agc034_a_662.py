'''
[A - Kenken Race](https://atcoder.jp/contests/agc034/tasks/agc034_a)
'''

n, a, b, c, d = map(int, input().split())
s = list(input())
a -= 1
b -= 1
c -= 1
d -= 1

flag = False
if c > d:
    for i in range(n-1):
        if b <= i <= d and s[i-1]+s[i]+s[i+1] == '...':
            flag = True
        if a <= i <= c and s[i] + s[i+1] == '##':
            flag = False
            break
else:
    for i in range(n-1):
        if a <= i <= d and s[i] + s[i+1] == '##':
            flag = False
            break
        else:
            flag = True

if flag:
    print('Yes')
else:
    print('No')
