'''
[C - Splitting Pile](https://atcoder.jp/contests/abc067/tasks/arc078_a)
'''

n = int(input())
A = list(map(int, input().split()))

sum_a = sum(A)

if n == 2:
    print(abs(A[0]-A[1]))
    exit()

min_diff = 10**9 + 1
first_sum = 0
for i in range(n-1):
    first_sum += A[i]
    second_sum = sum_a - first_sum
    diff = abs(first_sum - second_sum)
    if min_diff > diff:
        min_diff = diff

print(min_diff)
