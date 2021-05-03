import math


def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = math.sqrt(1 - 4*c)
    x_1 = 2*c//(-b + D)
    x_2 = 2*c//(-b - D)

    return x_1, x_2


n = int(input())
x1, x2 = solv_quadratic_equation(1, 1, -2*(n+1))
cut_num = math.floor(x2)

ans = n + 1 - cut_num
print(ans)
