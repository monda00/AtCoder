def is_atcoder(c):
    if c == 'a' or c == 't' or c == 'c' or c == 'o' or \
            c == 'd' or c == 'e' or c == 'r':
        return True
    else:
        return False

s1 = input()
s2 = input()

for c1, c2 in zip(s1, s2):
    if c1 == '@' and is_atcoder(c2):
        continue
    elif c2 == '@' and is_atcoder(c1):
        continue
    elif c1 == c2:
        continue
    else:
        print('You will lose')
        exit()
print('You can win')

