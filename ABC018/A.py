import collections

score = collections.OrderedDict()

score['taro'] = int(input())
score['jiro'] = int(input())
score['saburo'] = int(input())

sorted_score = collections.OrderedDict(
    sorted(score.items(), key=lambda x: x[1], reverse=True))
keys = list(sorted_score.keys())

print(keys.index('taro') + 1)
print(keys.index('jiro') + 1)
print(keys.index('saburo') + 1)

