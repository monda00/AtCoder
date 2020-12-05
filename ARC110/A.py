n = int(input())

li = [2, 3, 4, 5, 7, 9, 11, 13, 16, 17, 19, 23, 25, 29]

ans = 1
for i in li:
    if i <= n:
        ans *= i

if n >= 29:
    ans /= 2
    ans /= 4
    ans /= 5

ans = ans + 1
print(int(ans))
