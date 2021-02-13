'''
[B - 謎のたこ焼きおじさん](https://atcoder.jp/contests/arc008/tasks/arc008_2)
'''

from collections import Counter
import math

n, m = map(int, input().split())
name = list(input())
kit = list(input())

name_c = Counter(name)
kit_c = Counter(kit)

ans = 1
for key, value in name_c.items():
    if kit_c[key] != 0 and kit_c[key] < value:
        if math.ceil(value/kit_c[key]) > ans:
            ans = math.ceil(value/kit_c[key])

if len(set(name) - set(kit)) > 0:
    ans = -1

print(ans)
