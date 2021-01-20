'''
[D - Prediction and Restriction](https://atcoder.jp/contests/abc149/tasks/abc149_d)
'''

n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())
my = []

ans = 0
for i in range(n):
    if i < k:
        if t[i] == 'r':
            my.append('p')
            ans += p
        elif t[i] == 's':
            my.append('r')
            ans += r
        else:
            my.append('s')
            ans += s
    elif t[i] == t[i-k]:
        if t[i] == 'r':
            if my[i-k] == 'r':
                my.append('p')
                ans += p
            else:
                my.append(t[i])
        elif t[i] == 's':
            if my[i-k] == 's':
                my.append('r')
                ans += r
            else:
                my.append(t[i])
        else:
            if my[i-k] == 'p':
                my.append('s')
                ans += s
            else:
                my.append(t[i])
        continue
    else:
        if t[i] == 'r':
            my.append('p')
            ans += p
        elif t[i] == 's':
            my.append('r')
            ans += r
        else:
            my.append('s')
            ans += s

print(ans)
