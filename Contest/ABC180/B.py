import math

n = int(input())
x = list(map(int, input().split()))

m = 0
y = 0
t = list()
for i in range(len(x)):
    m += abs(x[i])
    y += x[i]**2
    t.append(abs(x[i]))

print(m)
print(math.sqrt(y))
print(max(t))
