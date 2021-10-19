'''
[B - Palindrome-phobia](https://atcoder.jp/contests/cf17-final/tasks/cf17_final_b)
'''

s = list(input())
a = s.count('a')
b = s.count('b')
c = s.count('c')

if max(a, b, c) - min(a, b, c) >= 2:
    print('NO')
else:
    print('YES')
