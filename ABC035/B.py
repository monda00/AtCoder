s = input()
t = int(input())
x = 0
y = 0
notknow = 0
for d in s:
    if d == 'L':
        x -= 1
    elif d == 'R':
        x += 1
    elif d == 'U':
        y += 1
    elif d == 'D':
        y -= 1
    else:
        notknow += 1

if t == 1:
    print(abs(x) + abs(y) + notknow)
else:
    sumxy = abs(x) + abs(y)
    if sumxy < notknow:
        print(abs((notknow - sumxy)%2))
    else:
        print(abs(abs(x) + abs(y) - notknow))

