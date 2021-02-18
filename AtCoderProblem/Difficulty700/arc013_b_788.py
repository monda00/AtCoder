'''
[B - 引越しできるかな？](https://atcoder.jp/contests/arc013/tasks/arc013_2)
'''

C = int(input())
min_c = []
midle_c = []
max_c = []
for _ in range(C):
    n, m, l = map(int, input().split())
    s = sorted([n, m, l])
    min_c.append(s[0])
    midle_c.append(s[1])
    max_c.append(s[2])

ans = max(min_c) * max(midle_c) * max(max_c)

print(ans)
