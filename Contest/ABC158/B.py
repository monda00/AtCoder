n, a, b = map(int, input().split())

num = n // (a + b)
rem = n % (a + b)

if rem - a <= 0:
    print(a * num + rem)
else:
    print(a * num + a)
