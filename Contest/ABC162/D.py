n = int(input())
s = input()
ans = s.count('R') * s.count('G') * s.count('B')

for i in range(n):
    for j in range(i+1, n-1):
        k = 2 * j - i
        if(k < n):
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                ans -= 1

print(ans)
