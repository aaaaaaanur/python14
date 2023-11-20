# Составить таблицу умножения
l = [2, 3, 4, 5, 6, 7, 8, 9]

for i in l:
    for x in l:
        a = i * x
        print(str(i), '*', str(x), '=', str(a))