low, hight = map(int, input().split())
n = int(input())
for _ in range(n):
    a = int(input())
    if a < low:
        print(low - a)
    elif a > hight:
        print(-1)
    else:
        print(0)

