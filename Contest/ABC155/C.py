n = int(input())
str_dic = {}
for _ in range(n):
    inp = input()
    if inp in str_dic:
        str_dic[inp] += 1
    else:
        str_dic[inp] = 1

max_num = max(str_dic.values())

max_str = [s[0] for s in str_dic.items() if s[1] == max_num]

for s in sorted(max_str):
    print(s)

