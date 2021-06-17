n = 3

patterns = []
for i in range(2**n):  # 1<<nとしているプログラムもある
    print('i:', i)
    p = [0] * n
    for j in range(n):
        print('  j:', j)
        # if i & (1 << j): # これでも可
        if i >> j & 1:  # 0からnまで右シフトして1とのANDをとることでビットが立っているか(1かどうか)判定
            print('    bit:', i >> j & 1)
            p[j] = 1
    patterns.append(p)

print(patterns)
