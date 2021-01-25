'''
[A - Diverse Word](https://atcoder.jp/contests/agc022/tasks/agc022_a)
'''
LAST = 'zyxwvutsrqponmlkjihgfedcba'

s = list(input())

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

for a in alphabet:
    if not a in s:
        s.append(a)
        print(''.join(s))
        exit()

if LAST == ''.join(s):
    print(-1)
    exit()

ans = LAST
for i in range(len(s)):
    tmp_s = s.copy()
    for j in range(i+1, len(s)):
        tmp_s[i], tmp_s[j] = tmp_s[j], tmp_s[i]
        if ''.join(s) < ''.join(tmp_s):
            if ''.join(tmp_s[:i+1]) < ans:
                ans = ''.join(tmp_s[:i+1])
        tmp_s[j], tmp_s[i] = tmp_s[i], tmp_s[j]

print(ans)
