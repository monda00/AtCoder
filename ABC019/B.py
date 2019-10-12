s = input()
ans_str = ""
str_count = 1
for i in range(len(s)):
    if i == len(s) - 1 or s[i] != s[i + 1]:
        ans_str += s[i] + str(str_count)
        str_count = 1
    else:
        str_count += 1
print(ans_str)

