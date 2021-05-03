sx, sy, gx, gy = map(int, input().split())

sy = -sy

a = (gy - sy) / (gx - sx)
b = sy - a*sx

ans = -1 * b / a

print(ans)
