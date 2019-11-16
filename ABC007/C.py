import queue

def can_go_to(x, y):
    if maze[x][y] == '.':
        return True
    else:
        return False

def set_dist(from_cell, to_cell):
    if maze[to_cell[0]][to_cell[1]] == '.':
        maze[to_cell[0]][to_cell[1]] = maze[from_cell[0]][from_cell[1]] + 1

row_num, column_num = map(int, input().split())
start_y, start_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())
start_x = start_x - 1
start_y = start_y - 1
goal_x = goal_x - 1
goal_y = goal_y - 1

maze = list()
cell_queue = queue.Queue()

for _ in range(row_num):
    maze.append(list(input()))

cell_queue.put([start_y, start_x])
maze[start_y][start_x] = 0
while(not cell_queue.empty()):
    current_cell = cell_queue.get()
    # 移動さきのマス
    up_cell = [current_cell[0] + 1, current_cell[1]]
    down_cell = [current_cell[0] - 1, current_cell[1]]
    right_cell = [current_cell[0], current_cell[1] + 1]
    left_cell = [current_cell[0], current_cell[1] - 1]

    if can_go_to(right_cell[0], right_cell[1]):
        set_dist(current_cell, right_cell)
        cell_queue.put(right_cell)
    if can_go_to(left_cell[0], left_cell[1]):
        set_dist(current_cell, left_cell)
        cell_queue.put(left_cell)
    if can_go_to(up_cell[0], up_cell[1]):
        set_dist(current_cell, up_cell)
        cell_queue.put(up_cell)
    if can_go_to(down_cell[0], down_cell[1]):
        set_dist(current_cell, down_cell)
        cell_queue.put(down_cell)

print(maze[goal_y][goal_x])

