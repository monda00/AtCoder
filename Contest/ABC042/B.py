n, l = map(int, input().split())
s_li = list()
for _ in range(n):
    s_li.append(input())

s_li.sort()
print(''.join(s_li))

