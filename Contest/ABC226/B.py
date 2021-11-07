n = int(input())

L = []
A = []
seq = set()
for _ in range(n):
    tmp = list(map(int, input().split()))
    L.append(tmp[0])
    A.append(tmp[1:])
    seq.add(' '.join(str(tmp[1:])))

print(len(list(seq)))
