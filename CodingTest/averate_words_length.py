sentence = input()

for p in "!?',;.":
    sentence = sentence.replace(p, '')

words = sentence.split()

ave_len = sum(map(len, words)) / len(words)

print(ave_len)
