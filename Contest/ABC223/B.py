s = list(input())

s_li = []
for i in range(len(s)):
    s_li.append(''.join(s[i:]+s[:i]))
s_li.sort()
print(s_li[0])
print(s_li[-1])
