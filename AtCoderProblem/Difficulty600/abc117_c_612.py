'''
https://atcoder.jp/contests/abc117/tasks/abc117_c
'''
n, m = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

if n >= m:
    print(0)
    exit()

d = [b - a for a, b in zip(X, X[1:])]
d.sort()
print(sum(d[:m - n]))
