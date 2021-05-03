n, k = map(int, input().split())
A = set()

for i in range(k):
    d = input()
    a = set(list(input().split()))
    A = A | a

print(n - len(A))
