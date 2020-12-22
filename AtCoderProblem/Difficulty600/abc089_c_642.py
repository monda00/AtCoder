'''
[C - March](https://atcoder.jp/contests/abc089/tasks/abc089_c)
'''

n = int(input())
s_li = list()
for _ in range(n):
    s_li.append(list(input()))

start_m = 0
start_a = 0
start_r = 0
start_c = 0
start_h = 0
for s in s_li:
    if s[0] == 'M':
        start_m += 1
    if s[0] == 'A':
        start_a += 1
    if s[0] == 'R':
        start_r += 1
    if s[0] == 'C':
        start_c += 1
    if s[0] == 'H':
        start_h += 1

march = [start_m, start_a, start_r, start_c, start_h]
ans = 0
for first_ind in range(len(march)):
    for second_ind in range(first_ind+1, len(march)):
        for third_ind in range(second_ind+1, len(march)):
            ans += (march[first_ind] * march[second_ind] * march[third_ind])

print(ans)
