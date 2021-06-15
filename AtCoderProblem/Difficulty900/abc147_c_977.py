'''
[C - HonestOrUnkind2](https://atcoder.jp/contests/abc147/tasks/abc147_c)
'''

n = int(input())
A = []
X = []
Y = []
for _ in range(n):
    a = int(input())
    A.append(a)
    x = []
    y = []
    for _ in range(a):
        _x, _y = map(int, input().split())
        x.append(_x-1)
        y.append(_y)
    X.append(x)
    Y.append(y)


ans = 0
# ビット探索で正直者を仮定する
for i in range(2**n):
    check = True
    honest = []
    for j in range(n):
        # 正直者だけ矛盾してないか判定
        if (i >> j) & 1:
            honest.append(j)
            for k in range(A[j]):
                if Y[j][k] != ((i >> X[j][k]) & 1):
                    check = False
                    break

    if check:
        ans = max(ans, len(honest))

print(ans)
