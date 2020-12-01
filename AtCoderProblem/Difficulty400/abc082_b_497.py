'''
[B - Two Anagrams](https://atcoder.jp/contests/abc082/tasks/abc082_b)
'''

s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

if s < t:
    print('Yes')
else:
    print('No')
