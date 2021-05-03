import math

n = int(input())
score = 1000000
for i in range(1, int(math.sqrt(n))+1):
    tmp_score = abs(i - (n // i)) + (n % i)
    if score > tmp_score:
        score = tmp_score
print(score)

