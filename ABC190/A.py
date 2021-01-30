a, b, c = map(int, input().split())

if c == 0:
    if a <= b:
        print('Aoki')
    elif a > b:
        print('Takahashi')
else:
    if a < b:
        print('Aoki')
    elif a >= b:
        print('Takahashi')
