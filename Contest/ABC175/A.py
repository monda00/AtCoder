s = input()

if s[0] == 'R' and s[1] == 'R' and s[2] == 'R':
    print(3)
elif (s[0] == 'R' and s[1] == 'R') or (s[1] == 'R' and s[2] == 'R'):
    print(2)
elif 'R' in s:
    print(1)
else:
    print(0)
