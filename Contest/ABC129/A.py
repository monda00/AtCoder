ab, bc, ca = map(int, input().split())

min_dis = 0
abbc = ab + bc
abca = ab + ca
bcca = bc + ca

print(min(abbc, abca, bcca))

