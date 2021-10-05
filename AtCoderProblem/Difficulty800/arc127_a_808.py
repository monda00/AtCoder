'''
[A - Leading 1s](https://atcoder.jp/contests/arc127/tasks/arc127_a)
'''

n = int(input())

digit = len(str(n))
ans = 0

for i in range(1, digit+1):
    l_1s = '1'*i
    l_1s2 = '1'*(i-1)+'2'
    #print('l_1s :', l_1s)
    #print('l_1s2:', l_1s2)
    for j in range(digit-i+1):
        if i == j == 0:
            continue
        inf = int(l_1s+'0'*j)
        if inf > n:
            break
        sup = min(int(l_1s2+'0'*j), n+1)
        #print('inf:', inf)
        #print('sup:', sup)
        ans += (sup-inf)
        #print('current ans:', ans)
print(ans)
