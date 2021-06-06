x, y = map(int, input().split())

if (x == 1 and y == 2) or (x == 2 and y == 1) or (x == 0 and y == 0):
    print(0)
if (x == 0 and y == 2) or (x == 2 and y == 0) or (x == 1 and y == 1):
    print(1)
if (x == 1 and y == 0) or (x == 0 and y == 1) or (x == 2 and y == 2):
    print(2)
