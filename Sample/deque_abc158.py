from collections import deque

s = input()
q = int(input())
query = []
for _ in range(q):
    query.append(list(input().split()))

que = deque(s)
reverse_flag = False
for i in range(q):
    if query[i][0] == '1':
        reverse_flag = not reverse_flag
    else:
        if query[i][1] == '1' and reverse_flag:
            que.append(query[i][2])
        elif query[i][1] == '1':
            que.appendleft(query[i][2])
        elif query[i][1] == '2' and reverse_flag:
            que.appendleft(query[i][2])
        else:
            que.append(query[i][2])

if reverse_flag:
    que.reverse()

print(''.join(que))
