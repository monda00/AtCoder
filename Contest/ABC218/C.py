import numpy as np

n = int(input())
S = []
T = []

for _ in range(n):
    tmp = list(input())
    S.append(tmp)

for _ in range(n):
    tmp = list(input())
    T.append(tmp)

S = np.array(S)
T = np.array(T)

for i in range(n):
    if np.all(S[i, :] == '.'):
        continue
    else:
        after_s = i
for i in range(n-1, -1, -1):
    if np.all(S[i, :] == '.'):
        continue
    else:
        before_s = i
S = S[before_s:after_s+1, :]
for i in range(n):
    if np.all(S[:, i] == '.'):
        continue
    else:
        after_s = i
for i in range(n-1, -1, -1):
    if np.all(S[:, i] == '.'):
        continue
    else:
        before_s = i
S = S[:, before_s:after_s+1]

for i in range(n):
    if np.all(T[i, :] == '.'):
        continue
    else:
        after_s = i
for i in range(n-1, -1, -1):
    if np.all(T[i, :] == '.'):
        continue
    else:
        before_s = i
T = T[before_s:after_s+1, :]
for i in range(n):
    if np.all(T[:, i] == '.'):
        continue
    else:
        after_s = i
for i in range(n-1, -1, -1):
    if np.all(T[:, i] == '.'):
        continue
    else:
        before_s = i
T = T[:, before_s:after_s+1]

for i in range(5):
    T = np.rot90(T).copy()
    if S.shape[0] == T.shape[0] and S.shape[1] == T.shape[1]:
        tmp_s = S.tolist()
        tmp_t = T.tolist()
        ok = True
        for j in range(S.shape[0]):
            if tmp_s[j] != tmp_t[j]:
                ok = False
        if ok:
            print('Yes')
            exit()

print('No')
