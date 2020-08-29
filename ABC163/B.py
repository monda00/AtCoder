N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_homework_day = sum(A)

if sum_homework_day > N:
    print(-1)
else:
    print(N - sum_homework_day)
