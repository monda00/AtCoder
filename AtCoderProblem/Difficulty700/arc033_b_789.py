'''
[B - メタ構文変数](https://atcoder.jp/contests/arc033/tasks/arc033_2)
'''

Na, Nb = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

union = len(A | B)
inter = len(A & B)

ans = inter / union
print(ans)
