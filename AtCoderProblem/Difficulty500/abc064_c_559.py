'''
[C - Colorful Leaderboard](https://atcoder.jp/contests/abc064/tasks/abc064_c)
'''

n = int(input())
A = list(map(int, input().split()))

grey = 0
brown = 0
green = 0
l_blue = 0
blue = 0
yellow = 0
orange = 0
red = 0
top = 0

for a in A:
    if 1 <= a <= 399:
        grey += 1
    elif 400 <= a <= 799:
        brown += 1
    elif 800 <= a <= 1199:
        green += 1
    elif 1200 <= a <= 1599:
        l_blue += 1
    elif 1600 <= a <= 1999:
        blue += 1
    elif 2000 <= a <= 2399:
        yellow += 1
    elif 2400 <= a <= 2799:
        orange += 1
    elif 2800 <= a <= 3199:
        red += 1
    else:
        top += 1

color = [grey, brown, green, l_blue, blue, yellow, orange, red]

num_c = 0
for c in color:
    if c > 0:
        num_c += 1

min_c = num_c
max_c = num_c

if min_c == 0 and top > 0:
    min_c = 1
if top > 0:
    max_c += top

print(min_c, max_c)
