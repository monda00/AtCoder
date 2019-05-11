'''
B - RGB Boxes
'''

r_weight, g_weight, b_weight, N = map(int, input().split())

ans = 0
for r in range(N+1):
    for g in range(N-r*r_weight+1):
        rem = N - r*r_weight - g*g_weight
        if rem % b_weight == 0 and rem >= 0:
            ans += 1

print(ans)

