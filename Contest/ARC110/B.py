n = int(input())
t = input()

len_110 = 3
if n % len_110 == 0:
    num_110 = n // len_110
else:
    num_110 = n // len_110 + 1

if t[0:2] == '10' and n % len_110 == 0:
    num_110 += 1
if t[0] == '0' and n % len_110 == 2:
    num_110 += 1
if t[0] == '0' and n % len_110 == 0:
    num_110 += 1

sub_110 = '110' * num_110

sub_num = 0
for start_idx in range(len_110*num_110):
    if sub_110[start_idx:start_idx+n] == t:
        sub_num += 1

all_num = 10 ** 10
ans = (all_num - num_110 + 1) * sub_num

print(ans)
