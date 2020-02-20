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
# c以下になる組み合わせがいくつあるか計算する
while l+1<r:
    c = (l + r) // 2
    print('c :', c)
    cnt = 0

    # 0になる組み合わせの個数のカウントを追加
    if c >= 0:
        cnt += n * len(zero)

    print(c//pos)
    print('c//pos: ', np.searchsorted(a, c//pos, side='right').sum())
    print('(-c-1)//(-neg): ',
          (n-np.searchsorted(a, (-c-1)//(-neg), side='right')).sum())
    cnt += np.searchsorted(a,c//pos,side='right').sum() + (n-np.searchsorted(a,(-c-1)//(-neg),side='right')).sum()
    cnt -= np.count_nonzero(a*a<=c)
    cnt//=2

    print('cnt :', cnt)

    if cnt >= k:
        l = c
    else:
        r = c

print(l)
