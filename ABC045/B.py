from collections import deque

s_a = deque(list(input()))
s_b = deque(list(input()))
s_c = deque(list(input()))

next_player = s_a.popleft()
while(len(s_a) >= 0 and len(s_b) >= 0 and len(s_c) >= 0):
    if next_player == 'a':
        if len(s_a) == 0:
            print('A')
            exit()
        next_player = s_a.popleft()
    if next_player == 'b':
        if len(s_b) == 0:
            print('B')
            exit()
        next_player = s_b.popleft()
    if next_player == 'c':
        if len(s_c) == 0:
            print('C')
            exit()
        next_player = s_c.popleft()

