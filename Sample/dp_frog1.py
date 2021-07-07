n = int(input())
h = list(map(int, input().split()))

c = [10**5+1] * n

c[0] = 0
c[1] = abs(h[1]-h[0])

for i in range(2, n):
    c[i] = min(abs(h[i]-h[i-1])+c[i-1], abs(h[i]-h[i-2])+c[i-2])

print(c[-1])
