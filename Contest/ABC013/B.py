a = int(input())
b = int(input())

can1 = abs(a - b)
can2 = min(a, b) + min(abs(10 - a), abs(10 - b))

if (can1 < can2):
    print(can1)
else:
    print(can2)

