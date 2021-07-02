import sys
sys.setrecursionlimit(10**7)  # 再起呼び出しの回数がデフォルトだと

H, W = map(int, input().split())
maze = [list(input()) for h in range(H)]

for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            sx, sy = h, w


def dfs(x, y):
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
        return

    if maze[x][y] == 'g':
        print('Yes')
        exit()

    maze[x][y] = '#'
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)


dfs(sx, sy)
print('No')
