a_500 = int(input())
b_100 = int(input())
c_50 = int(input())
x_sum = int(input())

cnt = 0
for a in range(a_500+1):
    for b in range(b_100+1):
        for c in range(c_50+1):
            if 500*a + 100*b + 50*c == x_sum:
                cnt += 1

print(cnt)

