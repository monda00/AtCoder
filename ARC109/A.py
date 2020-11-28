a, b, x, y = map(int, input().split())

if a-b == 1 and x+y > x:
    print(x)
elif b-a == 1 and 3*x > x+y:
    print(x+y)
elif a < b and 2*x <= y:
    print(2*x*(b-a) + x)
elif a > b and 2*x <= y:
    print(2*x*(a-b) - x)
elif a > b:
    print((abs(a-b)-1)*y+x)
elif a != b:
    print(abs(a-b)*y+x)
else:
    print(x)
