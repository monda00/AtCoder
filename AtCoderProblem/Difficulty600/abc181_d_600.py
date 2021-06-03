'''
[D - Hachi](https://atcoder.jp/contests/abc181/tasks/abc181_d)
'''

from collections import Counter

s = list(input())
c = Counter(s)

if len(s) == 1 and s[0] == '8':
    print('Yes')
    exit()

if len(s) == 2:
    eight = 16
    while True:
        e_c = Counter(list(str(eight)))
        ok = True
        for k in e_c.keys():
            if e_c[k] > c[k]:
                ok = False
        if ok:
            print('Yes')
            exit()
        eight += 8
        if eight > 100:
            break

eight = 104
while True:
    e_c = Counter(list(str(eight)))
    ok = True
    for k in e_c.keys():
        if e_c[k] > c[k]:
            ok = False
    if ok:
        print('Yes')
        exit()
    eight += 8
    if eight > 1000:
        break

print('No')
