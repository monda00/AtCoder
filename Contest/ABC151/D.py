import queue
INF = 100000000

n, m = map(int, input().split())
maze = list()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    maze.append(list(input()))


def bfs(sx, sy):
    """
    幅優先探索で迷路の最短経路を計算する。

    Parameters
    ----------
    sx : int
        スタートのx座標
    sy : int
        スタートのy座標

    Returns
    ----------
    ans : int
        迷路の最短経路
    """
    que = queue.Queue()
    d = [[INF] * m for _ in range(n)]
    que.put([sx, sy])
    d[sx][sy] = 0
    max_d = 0

    while not que.empty():
        p = que.get()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and d[nx][ny] == INF:
                que.put([nx, ny])
                d[nx][ny] = d[p[0]][p[1]] + 1
                if d[nx][ny] > max_d:
                    max_d = d[nx][ny]

    return max_d


ans = 0
for sx in range(n):
    for sy in range(m):
        if maze[sx][sy] == '#':
            continue
        d = bfs(sx, sy)
        if d > ans:
            ans = d

print(ans)
