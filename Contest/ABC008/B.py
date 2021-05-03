n = int(input())
vote = {}
for _ in range(n):
    cand = input()
    if cand in vote:
        vote[cand] += 1
    else:
        vote[cand] = 0

print(max(vote, key=vote.get))

