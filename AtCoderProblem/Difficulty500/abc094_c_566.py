'''
[C - Many Medians](https://atcoder.jp/contests/abc094/tasks/arc095_a)
'''

n = int(input())
X = list(map(int, input().split()))

X_sort = sorted(X)

for i in range(n):
    medi = X_sort[(n//2)-1]
    if medi < X[i]:
        print(medi)
    else:
        print(X_sort[(n//2)])
