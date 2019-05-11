'''
C - AB Substrings
'''

str_list = []
end_a = []
start_b = []
ab_num = 0
for i in range(int(input())):
    str_list.append(input())
    if 'AB' in str_list[-1]:
        ab_num += 1
    if str_list[-1].endswith('A'):
        end_a.append(i)
    if str_list[-1].startswith('B'):
        start_b.append(i)

if end_a == start_b:
    ab_num += min(len(end_a), len(start_b)) - 1
else:
    ab_num += min(len(end_a), len(start_b))

print(ab_num)

