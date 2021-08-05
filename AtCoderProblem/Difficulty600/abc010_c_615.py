import math

startx, starty, endx, endy, limittime, v = map(int, input().split())
n = int(input())
X, Y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


for i in range(n):
    sum_d = calc_dist(startx, starty, X[i], Y[i]) + \
        calc_dist(X[i], Y[i], endx, endy)
    if sum_d / v <= limittime:
        print('YES')
        exit()

print('NO')
