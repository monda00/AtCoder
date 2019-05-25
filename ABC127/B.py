r, D, x_2000 = map(int, input().split())

x_pre = x_2000
for i in range(1, 11):
    x = r * x_pre - D
    print(x)
    x_pre = x

