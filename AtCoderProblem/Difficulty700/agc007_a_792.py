'''
[A - Shik and Stone](https://atcoder.jp/contests/agc007/tasks/agc007_a)
'''

h, w = map(int, input().split())
A = []
for _ in range(h):
    A.append(list(input()))


def exist_left(col):
    for i in range(h):
        for j in range(col):
            if A[i][j] == '#':
                return True
    return False


def exist_up(row):
    for i in range(row):
        for j in range(w):
            if A[i][j] == '#':
                return True
    return False


i = 0
j = 0
while True:
    A[i][j] = '.'

    if i < h-1 and j < w-1:
        if A[i+1][j] == "#" and not exist_up(i+1):
            i += 1
        elif A[i][j+1] == "#" and not exist_left(j+1):
            j += 1
        else:
            print('Impossible')
            exit()
    elif i < h-1:
        if A[i+1][j] == "#" and not exist_up(i+1):
            i += 1
        else:
            print('Impossible')
            exit()
    elif j < w-1:
        if A[i][j+1] == "#" and not exist_left(j+1):
            j += 1
        else:
            print('Impossible')
            exit()
    else:
        print('Impossible')
        exit()

    if i == h-1 and j == w-1:
        break

print('Possible')
