n = int(input())
A = list(map(int, input().split()))

sub_sum = 0
max_sub_sum = 0
pos = 0
max_pos = 0

for i in range(n):
    sub_sum += A[i]
    max_sub_sum = max(max_sub_sum, sub_sum)
    max_pos = max(max_pos, pos+max_sub_sum)
    pos += sub_sum

print(max_pos)
