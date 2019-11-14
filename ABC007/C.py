row_num, column_num = map(int, input().split())
start_y, start_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())

maze = list()

for _ in range(row_num):
    maze.append(list(input()))

print(maze)
