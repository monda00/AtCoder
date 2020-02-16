def calc_distance(maze, sx, sy):
    maze[sx][sy] = 'S'

    # Goalまでの距離としてはあり得ない数値を設定
    INF = 100000000

    field_x_length = len(maze[0])
    field_y_length = len(maze)

    # mazeと同じ配列構造で全てINFの二次元配列を作る
    distance = []
    for i in range(field_y_length):
        distance.append([])
        for j in range(field_x_length):
            if maze[i][j] == '#':
                distance[i].append(-1)
            else:
                distance[i].append(INF)

    # queue配列を作り、ここに座標を格納する
    queue = []

    # queueの末尾にStart座標を入れる
    queue.insert(0, (sy, sx))

    # Startの座標距離は0に設定
    distance[sy][sx] = 0

    # 全てのマスが埋まるまで
    while True:
        # 最初に入れた要素を取り出す
        y, x = queue.pop()

        # INFの値が無くなったら終了
        if not INF in distance:
            break

        # 新しい座標(ny, nx)に現時点の座標から
        # (0, 1)(1, 0)(0, -1)(-1, 0)移動した値を代入
        for i in range(0, 4):
            nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

            # 移動先ny, nxが迷路の範囲内
            # かつ壁（maze配列が#）でなく、
            # かつ未到達（distance配列がINF）であるときに
            # 現時点の距離+1をdistance配列に格納する
            # 現時点の座標をqueue配列に格納する（再ループの時にその座標から始める）
            if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and maze[ny][nx] != '#' and distance[ny][nx] == INF):
                queue.insert(0, (ny, nx))
                distance[ny][nx] = distance[y][x] + 1

    # 全ての値を埋めたら、最も遠い点の距離を返す
    return max(distance)

height, wedth = map(int, input().split())
maze_original = list()
for _ in range(height):
    maze_original.append(list(input()))

print(calc_distance(maze_original, 0, 0))
print(calc_distance(maze_original, 0, 1))
print(calc_distance(maze_original, 0, 2))
print(maze_original)

