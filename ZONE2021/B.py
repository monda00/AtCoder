N, D, H = map(int, input().split())
d = []
h = []

for _ in range(N):
    d_in, h_in = map(int, input().split())
    d.append(d_in)
    h.append(h_in)

ans_li = []
for i in range(N):
    a = (h[i] - H) / (d[i] - D)
    b = H - D * a
    ans_li.append(b)

ans = max(ans_li)

if ans < 0:
    ans = 0

print(ans)
