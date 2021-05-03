w, h, n = map(int, input().split())

x_min = 0
y_min = 0
x_max = w
y_max = h
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and x_min < x:
        x_min = x
    elif a == 2 and x_max > x:
        x_max = x
    elif a == 3 and y_min < y:
        y_min = y
    elif a == 4 and y_max > y:
        y_max = y
if x_max < x_min or y_max < y_min:
    print(0)
else:
    print((x_max - x_min) * (y_max - y_min))

