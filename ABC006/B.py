n = int(input())
a_0 = 0
a_1 = 0
a_2 = 1
if n == 1:
    print(a_0)
elif n == 2:
    print(a_1)
elif n == 3:
    print(a_2)
else:
    for i in range(3, n):
        a = a_0 + a_1 + a_2
        a_0 = a_1
        a_1 = a_2
        a_2 = a
    print(a % 10007)

