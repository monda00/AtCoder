h, w, n = map(int, input().split())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ind = []
col = []

for i in range(n):
    ind.append([A[i], i])
    col.append([B[i], i])

ind.sort()
col.sort()

ind_cnt = 1
col_cnt = 1
ind_now = ind[0][0]
col_now = col[0][0]
ind[0].append(1)
col[0].append(1)
for i in range(1, n):
    if ind_now == ind[i][0]:
        ind[i].append(ind_cnt)
    else:
        ind_cnt += 1
        ind[i].append(ind_cnt)
    ind_now = ind[i][0]

    if col_now == col[i][0]:
        col[i].append(col_cnt)
    else:
        col_cnt += 1
        col[i].append(col_cnt)
    col_now = col[i][0]

ind.sort(key=lambda x: x[1])
col.sort(key=lambda x: x[1])

for i in range(n):
    print(ind[i][2], col[i][2])
