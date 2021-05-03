x, y = map(int, input().split())

lose = min([x, y])
win = max([x, y])

if lose + 3 > win:
    print('Yes')
else:
    print('No')
