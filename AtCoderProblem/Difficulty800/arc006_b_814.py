'''
[B - あみだくじ](https://atcoder.jp/contests/arc006/tasks/arc006_2)
'''

n, l = map(int, input().split())
lot = []
for _ in range(l+1):
    lot.append(list(input()))

len_lot = len(lot[0])

for i in range(n):
    d = i * 2
    r = 0
    frm = 'ver'
    while True:
        if d > 1 and frm != 'hori':
            if lot[r][d-1] == '-':
                d -= 2
                frm = 'hori'
            elif d < len_lot-1:
                if lot[r][d+1] == '-':
                    d += 2
                    frm = 'hori'
                else:
                    r += 1
                    frm = 'ver'
            else:
                r += 1
                frm = 'ver'
        elif d < len_lot-1 and frm != 'hori':
            if lot[r][d+1] == '-':
                d += 2
                frm = 'hori'
            else:
                r += 1
                frm = 'ver'
        else:
            r += 1
            frm = 'ver'

        if r == l:
            if lot[r][d] == 'o':
                print(i+1)
                exit()
            break
