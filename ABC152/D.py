n = int(input())

c = [[0 for i in range(10)] for j in range(10)]
for k in range(1, n+1):
    str_k = str(k)
    i = int(str_k[0])
    j = int(str_k[-1])
    c[i][j] += 1

answer = 0
for i in range(10):
    for j in range(10):
        answer += c[i][j] * c[j][i]

print(answer)

