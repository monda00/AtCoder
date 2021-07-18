'''
[D - Road to Millionaire](https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d)
'''

n = int(input())
A = list(map(int, input().split()))
money = 1000
stock = 0

for i in range(n-1):
    stock = 0
    if A[i] < A[i+1]:
        stock = money // A[i]
    money += (A[i+1]-A[i]) * stock

print(money)
