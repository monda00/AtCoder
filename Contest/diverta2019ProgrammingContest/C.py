'''
C - AB Substrings
'''

str_list = []
ab_num = 0
c1 = 0
c2 = 0
c3 = 0
for i in range(int(input())):
    str_list.append(input())
    ab_num += str_list[-1].count('AB')
    if str_list[-1].endswith('A') and str_list[-1].startswith('B'):
        c1 += 1
    elif str_list[-1].startswith('B'):
        c2 += 1
    elif str_list[-1].endswith('A'):
        c3 += 1

if c1 == 0:
    print(ab_num + min(c2, c3))
elif c2 + c3 == 0:
    print(ab_num + c1 - 1)
else:
    print(ab_num + c1 + min(c2, c3))

