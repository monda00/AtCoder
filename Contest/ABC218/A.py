n = int(input())
s = list(input())


for i in range(len(s)):
    if i == n-1:
        if s[i] == 'o':
            print('Yes')
        else:
            print('No')
