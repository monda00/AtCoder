n, k = map(int, input().split())
h = list(map(int, input().split()))

c = [10**5+1] * n

c[0] = 0
c[1] = abs(h[1]-h[0])

for i in range(2, n):
    c[i] = c[i-1] + abs(h[i]-h[i-1])
    for j in range(2, k+1):
        if i - j >= 0:
            c[i] = min(abs(h[i]-h[i-j])+c[i-j], c[i])

print(c[-1])
