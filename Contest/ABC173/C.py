import itertools
import copy

H, W, k = map(int, input().split())
matrix = []

for h in range(H):
    matrix.append(list(input()))

def count_black(mat):
    flat = list(itertools.chain.from_iterable(mat))
    b_sum = flat.count('#')
    return b_sum

ans = 0
for h in range(2 ** H):
    for w in range(2 ** W):
        tmp_matrix = copy.deepcopy(matrix)
        for i in range(H):
            if (h >> i) & 1:
                tmp_matrix[i][:] = ['.'] * W
        for j in range(W):
            if (w >> j) & 1:
                for i in range(H):
                    tmp_matrix[i][j] = '.'
        c = count_black(tmp_matrix)
        if c == k:
            ans += 1

print(ans)
