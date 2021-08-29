xy = list(input())

y = int(xy[-1])
x = ''.join(xy[:-2])

if 0 <= y <= 2:
    print(x + '-')
elif 3 <= y <= 6:
    print(x)
else:
    print(x + '+')
