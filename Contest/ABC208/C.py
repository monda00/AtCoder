n, k = map(int, input().split())
A = list(map(int, input().split()))

A_dic = []
for i in range(n):
    A_dic.append([i, A[i]])
A_dic.sort(key=lambda x: x[1])

ans = [0] * n
for i in range(n):
    tmp = k // n
    k_r = k % n
    if i < k_r:
        tmp += 1
    ans[A_dic[i][0]] = tmp

for i in range(n):
    print(ans[i])
