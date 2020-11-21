s, p = map(int, input().split())


def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return x_1, x_2


x1, x2 = solv_quadratic_equation(1, -s, p)

m = x1
n = s - m
if n * m == p:
    print('Yes')
    exit()

m = x2
n = s - m
if n * m == p:
    print('Yes')
    exit()

print('No')
