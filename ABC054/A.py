a, b = map(int, input().split())
if a == b:
    print('Draw')
elif a > b:
    if b == 1:
        print('Bob')
    else:
        print('Alice')
else:
    if a == 1:
        print('Alice')
    else:
        print('Bob')

