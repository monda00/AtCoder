'''
[C - ID](https://atcoder.jp/contests/abc113/tasks/abc113_c)
'''

from collections import defaultdict

n, m = map(int, input().split())
P = []
Y = []
P_dic = defaultdict(list)
ans = defaultdict(lambda: defaultdict(list))
for i in range(m):
    p, y = map(int, input().split())
    P.append(p)
    Y.append(y)

for i in range(m):
    P_dic[P[i]].append(Y[i])

for p in P_dic:
    P_dic[p].sort()

for p in P_dic:
    for i in range(len(P_dic[p])):
        p_id = str(p).zfill(6)
        y_id = str(i+1).zfill(6)
        ans[p][P_dic[p][i]].append(p_id+y_id)

for i in range(m):
    print(*ans[P[i]][Y[i]])
