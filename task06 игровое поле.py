# Имеется игровое поле размером 10 на 10. Колонки и строки обозначаюся буквами от а до j.
# Написать функцию, которая преобразует введеные координаты в формате "{x}{x}" - где x - это буква от a до j - в координаты игрового поля - {число},{число}
# Пример: функия принимает "ce" и преобразует это в координаты (3, 5), тк с - соответствует 3й колонке, а e 5й строке

d = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10
}
def convertCoordinates(coord):
    x1 = coord[0]  # c
    x2 = coord[1]  # e
    c1 = d[x1]
    c2 = d[x2]
    print(f'Координаты {c1}, {c2}')


convertCoordinates("ce")