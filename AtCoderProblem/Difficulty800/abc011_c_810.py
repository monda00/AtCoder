'''
[C - 123引き算](https://atcoder.jp/contests/abc011/tasks/abc011_3)
'''

n = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())

ng = [ng1, ng2, ng3]
ng.sort()

ans = 'YES'
for i in range(100):
    if n == ng1 or n == ng2 or n == ng3:
        ans = 'NO'
        break
    if n - 3 != ng1 and n - 3 != ng2 and n - 3 != ng3:
        n -= 3
    elif n - 2 != ng1 and n - 2 != ng2 and n - 2 != ng3:
        n -= 2
    elif n - 1 != ng1 and n - 1 != ng2 and n - 1 != ng3:
        n -= 1
    else:
        ans = 'NO'
        break
    if n < 0:
        break

if n > 0:
    ans = 'NO'

print(ans)
