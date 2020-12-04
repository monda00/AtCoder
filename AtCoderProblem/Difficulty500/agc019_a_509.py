'''
[A - Ice Tea Store](https://atcoder.jp/contests/agc019/tasks/agc019_a)
'''

q, h, s, d = map(int, input().split())
n = int(input())
v_per_1 = [4*q, 2*h, s, d//2]
v = [q, h, s, d]
min_index = v_per_1.index(min(v_per_1))

if min_index == 0:
    ans = n * (4 * q)
elif min_index == 1:
    ans = n * (2 * h)
elif min_index == 2:
    ans = n * s
else:
    ans = (n // 2) * d
    n = n % 2
    v_per_1_without_2 = [4*q, 2*h, s]
    min2_index = v_per_1_without_2.index(min(v_per_1_without_2))
    if min2_index == 0:
        ans += (4 * q) * n
    elif min2_index == 1:
        ans += (2 * h) * n
    else:
        ans += s * n

print(ans)
