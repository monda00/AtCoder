w = input()
beautiful_string = {}
for c in w:
    if c in beautiful_string:
        beautiful_string[c] += 1
    else:
        beautiful_string[c] = 1
for b in beautiful_string.values():
    if b % 2 != 0:
        print('No')
        exit()
print('Yes')

