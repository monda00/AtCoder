s = input()
k = int(input())
pwd_set = set()
for i in range(len(s)-k+1):
    pwd_set.add(s[i:i+k])
print(len(pwd_set))

