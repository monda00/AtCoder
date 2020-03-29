n, x, y = map(int, input().split())
dis_n = [0] * (n-1)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        dis_n[min([abs(j-i), abs(x-i)+1+abs(j-y), abs(y-i)+1+abs(j-x)])-1] += 1

for d in dis_n:
    print(d)
