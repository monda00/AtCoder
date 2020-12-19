'''
[A - XOR Circle](https://atcoder.jp/contests/agc035/tasks/agc035_a)
'''

import collections

n = int(input())
a = list(map(int, input().split()))

a_c = collections.Counter(a)

if a_c[0] == n:
    print('Yes')
    exit()

if a_c[0] == n//3 and len(a_c) == 2 and n % 3 == 0:
    print('Yes')
    exit()

if len(a_c) == 3 and n % 3 == 0:
    for a_ind in a_c:
        if a_c[a_ind] == n//3:
            continue
        else:
            print('No')
            exit()
    set_a = list(set(a))
    xor = set_a[0] ^ set_a[1] ^ set_a[2]
    if xor == 0:
        print('Yes')
        exit()
    else:
        print('No')
        exit()

print('No')
