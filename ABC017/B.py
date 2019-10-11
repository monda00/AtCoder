x = input()

for i in range(len(x)):
    if x[i] == 'o' or x[i] == 'k' or x[i] == 'u':
        continue
    elif x[i] == 'c' and i + 1 < len(x):
        if x[i + 1] == 'h':
            continue
        else:
            print('NO')
            exit()
    elif x[i] == 'h' and i > 0:
        if x[i - 1] == 'c':
            continue
        else:
            print('NO')
            exit()
    else:
        print('NO')
        exit()
print('YES')


