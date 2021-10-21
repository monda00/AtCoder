'''
[B - ニコニコ文字列](https://atcoder.jp/contests/dwango2015-prelims/tasks/dwango2015_prelims_2)
'''

import re

s = input()
pattern = '((25)+)'

ans = 0

repatter = re.compile(pattern)
result = repatter.findall(s)

for r in result:
    l = len(r[0]) // 2
    ans += l * (l + 1) // 2

print(ans)
