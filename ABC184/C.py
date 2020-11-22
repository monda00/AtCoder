r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
d_x = [0, 1, 2, 3, -1, -2, -3, 0, 0, 0, 0, 0, 0, 1, 1,
       1, 1, 2, 2, 2, 2, -1, -1, -1, -1, -2, -2, -2, -2]
d_y = [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, -1, -2, -3, 1, 2, -
       1, -2, 1, 2, -1, -2, 1, 2, -1, -2, 1, 2, -1, -2]

ans = 0

if r1 == r2 and c1 == c2:
    ans = 0
elif r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
    ans = 1
else:
    for dx, dy in zip(d_x, d_y):
        if r1+c1 == r2+dx+c2+dy or r1-c1 == r2+dx-c2+dy or abs(r1-r2+dx)+abs(c1-c2+dy) <= 3:
            ans = 2
            break
        else:
            ans = 3
    b1 = c1 - r1
    b2 = c2 + r2
    if (b1 + b2) % 2 == 0:
        ans = 2

print(ans)
