n = int(input())

ball = n
proc = []
while ball != 0:
    if ball % 2 == 0:
        ball //= 2
        proc.append('B')
    else:
        proc.append('A')
        ball -= 1

proc.reverse()
print(''.join(proc))
