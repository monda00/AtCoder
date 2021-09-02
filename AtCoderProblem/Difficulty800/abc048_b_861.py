'''
[B - Between a and b ...](https://atcoder.jp/contests/abc048/tasks/abc048_b)
'''

a, b, x = map(int, input().split())

if a % x == 0:
    start_divisible = x * (a//x)
else:
    start_divisible = x * (a//x + 1)
diff = b - start_divisible
ans = diff // x + 1

print(ans)
