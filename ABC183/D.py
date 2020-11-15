import numpy as np

n, w = map(int, input().split())
d = np.zeros(200005)
for _ in range(n):
    s, t, p = map(int, input().split())
    d[s] += p
    d[t] -= p

for i in range(len(d)-1):
    d[i+1] += d[i]

for i in range(len(d)):
    if d[i] > w:
        print('No')
        exit()
print('Yes')
