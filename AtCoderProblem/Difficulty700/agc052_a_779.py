'''
[A - Long Common Subsequence](https://atcoder.jp/contests/agc052/tasks/agc052_a)
'''

t = int(input())

N = []
S1 = []
S2 = []
S3 = []

for _ in range(t):
    N.append(int(input()))
    S1.append(int(input()))
    S2.append(int(input()))
    S3.append(int(input()))

for i in range(t):
    print('0'*N[i] + '1'*N[i] + '0')
