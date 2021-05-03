n = int(input())
a, b = map(int, input().split())
k = int(input())
p_li = list(map(int, input().split()))

if a in p_li or b in p_li or len(p_li) != len(set(p_li)):
    print('NO')
else:
    print('YES')

