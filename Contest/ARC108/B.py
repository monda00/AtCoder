N = int(input())
s = str(input())
t = ''

while not s == '':
    t += s[0]
    s = s[1:]
    if t[-3:] == 'fox':
        t = t[:-3]

print(len(t))
