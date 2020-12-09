'''
[B - 音楽ゲーム](https://atcoder.jp/contests/arc016/tasks/arc016_2)
'''

n = int(input())
score_board = list()

for _ in range(n):
    score_board.append(list(input()))

x_num = sum(1 for score in score_board for s in score if s == 'x')

o_num = 0
cols = [False, False, False, False, False, False, False, False, False]
for i in range(n-1, -1, -1):
    for j in range(9):
        if cols[j] and score_board[i][j] != 'o':
            cols[j] = False
        elif (not cols[j]) and score_board[i][j] == 'o':
            o_num += 1
            cols[j] = True

ans = x_num + o_num

print(ans)
