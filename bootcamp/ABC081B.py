import numpy as np

n = int(input())
nums = np.array(list(map(int, input().split())))

div_num = 0
while True:
    if np.any(nums % 2 == 1):
        break
    else:
        div_num += 1
        nums = nums / 2

print(div_num)

