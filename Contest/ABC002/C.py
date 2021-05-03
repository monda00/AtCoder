def calculateTriangle(x_1, y_1, x_2, y_2, x_3, y_3):
    return abs((x_1 - x_3)*(y_2 - y_3) - (x_2 - x_3)*(y_1 - y_3)) / 2.0

x_1, y_1, x_2, y_2, x_3, y_3 = map(int, input().split())
print(calculateTriangle(x_1, y_1, x_2, y_2, x_3, y_3))

