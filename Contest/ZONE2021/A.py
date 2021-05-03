s = list(input())

ans = 0
for i in range(len(s)-3):
    if ''.join(s[i:i+4]) == "ZONe":
        ans += 1

print(ans)
