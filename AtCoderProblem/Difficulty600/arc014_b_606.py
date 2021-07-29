'''
[B - あの日したしりとりの結果を僕達はまだ知らない。](https://atcoder.jp/contests/arc014/tasks/arc014_2)
'''

n = int(input())
w = []
for _ in range(n):
    w.append(input())

pre_w = w[0]
used = set()
used.add(pre_w)
for i in range(1, n):
    win = True
    if pre_w[-1] == w[i][0]:
        if not w[i] in used:
            used.add(w[i])
            pre_w = w[i]
        else:
            win = False
    else:
        win = False

    if not win and i % 2 == 0:
        print('LOSE')
        exit()
    elif not win and i % 2 == 1:
        print('WIN')
        exit()

print('DRAW')
