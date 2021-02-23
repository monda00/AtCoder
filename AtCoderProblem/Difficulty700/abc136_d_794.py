'''
[D - Gathering Children](https://atcoder.jp/contests/abc136/tasks/abc136_d)
'''
s = list(input())

dir = 'R'
ch = []
deli = []
for i in range(len(s)):
    if dir == 'R' and s[i] == 'L':
        dir = 'L'
        deli.append([i-1, i])
    elif dir == 'L' and s[i] == 'R':
        ch.append(i)
        dir = 'R'
ch.append(len(s))

move = 10 ** 100
ans = [0] * len(s)
start_i = 0
for c in range(len(ch)):
    for i in range(start_i, ch[c]):
        if i <= deli[c][0]:
            if (move-(deli[c][0]-i)) % 2 == 1:
                ans[deli[c][1]] += 1
            else:
                ans[deli[c][0]] += 1
        else:
            if (move-(i-deli[c][1])) % 2 == 1:
                ans[deli[c][0]] += 1
            else:
                ans[deli[c][1]] += 1
    start_i = ch[c]

print(*ans)
