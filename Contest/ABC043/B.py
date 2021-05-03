s = input()
res = ""
for input_c in s:
    if input_c == 'B':
        res = res[:-1]
    else:
        res += input_c
print(res)

