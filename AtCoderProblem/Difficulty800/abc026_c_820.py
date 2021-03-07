'''
[C - 高橋君の給料](https://atcoder.jp/contests/abc026/tasks/abc026_c)
'''

import collections

n = int(input())
B = [-1]
for _ in range(n-1):
    B.append(int(input())-1)

emp = [[] for _ in range(n)]

# 部下リストを作成
for i in range(n):
    for j in range(n):
        if i == B[j]:
            emp[i].append(j)

salary = [1] * n

for _ in range(20):
    for i in range(n):
        if emp[i]:
            li = []
            for e in emp[i]:
                li.append(salary[e])
            salary[i] = max(li) + min(li) + 1

print(salary[0])
