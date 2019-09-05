import statistics

l = list()
l = map(int, input().split())
median = statistics.median(l)
print(median)

