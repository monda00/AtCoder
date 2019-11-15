import queue

def can_go_to(x, y):
    if maze[x][y] == '#':
        return False
    else:
        return True

row_num, column_num = map(int, input().split())
start_y, start_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())

maze = list()
cell_queue = queue.Queue()

for _ in range(row_num):
    maze.append(list(input()))

cell_queue.put([start_x, start_y])
maze[start_x][start_y] = 0
while(not cell_queue.empty()):
    current_cell = cell_queue.get()
    # 移動さきのマス
    right_cell = [current_cell[0] + 1, current_cell[1]]
    left_cell = [current_cell[0] - 1, current_cell[1]]
    up_cell = [current_cell[0], current_cell[1] + 1]
    down_cell = [current_cell[0], current_cell[1] - 1]

    if can_go_to(right_cell[0], right_cell[1]):
        cell_queue.put(right_cell)
    if can_go_to(left_cell[0], left_cell[1]):
        cell_queue.put(left_cell)
    if can_go_to(up_cell[0], up_cell[1]):
        cell_queue.put(up_cell)
    if can_go_to(down_cell[0], down_cell[1]):
        cell_queue.put(down_cell)

