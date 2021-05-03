import numpy as np

point_num, dim_num = map(int, input().split())

points = []
for i in range(point_num):
    points.append(np.array(list(map(int, input().split()))))

ans = 0
for i in range(point_num):
    for j in range(i+1, point_num):
        dist = np.linalg.norm(points[i] - points[j])
        if(dist == int(dist)):
            ans += 1

print(ans)

