x = list(map(int, input()))

if x[0] == x[1] == x[2] == x[3]:
    print('Weak')
    exit()

cnt = 0
for i in range(3):
    if x[i] != 9 and x[i]+1 == x[i+1]:
        cnt += 1
    if x[i] == 9 and x[i+1] == 0:
        cnt += 1

if cnt == 3:
    print('Weak')
else:
    print('Strong')
