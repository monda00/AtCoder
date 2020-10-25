n = int(input())
a = list(map(int, input().split()))

a_set = set(a)

if len(a_set) == n:
    print('YES')
else:
    print('NO')
