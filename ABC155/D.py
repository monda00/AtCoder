import numpy as np

n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))
a.sort()

zero = a[a==0]
pos = a[a>0]
neg = a[a<0]

l = -10**18
r = 10**18

# 二分探索
# x以下になる組み合わせがいくつあるか計算する
while l+1<r:
    x = (l + r) // 2
    print('x :', x)
    cnt = 0

    # 0になる組み合わせの個数のカウントを追加
    if x >= 0:
        cnt += n * len(zero)

    print('x//pos: ', x//pos)
    print('pos: ', a.searchsorted(x//pos,side='right'))
    print('-(-x//neg): ', -(-x//neg))
    print('neg: ', (n-a.searchsorted(-(-x//neg),side='right')))
    cnt += a.searchsorted(x//pos,side='right').sum()
    cnt += (n-a.searchsorted(-(-x//neg),side='left')).sum()
    cnt -= np.count_nonzero(a*a<=x)
    cnt//=2

    print('cnt :', cnt)

    if cnt >= k:
        r = x
    else:
        l = x

print(r)
