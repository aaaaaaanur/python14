# написать функцию, которая находит корни квадратного уравнения

# a, b, c - коэффициенты квадратного уравнения
def calc(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D > 0:
        x1 = (-b + (D ** (1 / 2))) / (2 * a)
        x2 = (-b - (D ** (1 / 2))) / (2 * a)
        print('Ответ: x1 =', int(x1), ' x2 =', int(x2))
    elif D == 0:
        x = -(b / (2 * a))
        print('Ответ: x =', int(x))
    else:
        print('Квадратное уравнение не имеет корней')

calc(3, -5, 1)