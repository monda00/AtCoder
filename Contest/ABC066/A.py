import numpy as np
bell_li = list(map(int, input().split()))
bell_np = np.array(bell_li)
bell_np_sorted = bell_np.argsort()
print(bell_li[bell_np_sorted[0]] + bell_li[bell_np_sorted[1]])

