a = int(input())

maxA = 0
for i in range(a):
    x = i
    y = a - i
    tmp = x * y
    if maxA < tmp:
        maxA = tmp
print(maxA)

