
l = [7, 12, 33, 2, 54, 16, 13, 52, 1, 39, 42]
l2 = [7, 12, 33, 2, 52, 39, 42]


# найти минимальное значение
# найти максимальное значение
# найти среднее арифметическое
# найти все значения больше среднего арифметического и добавить в list


def minimum(length):
    min1 = length[0]
    for i in length:
        if i < min1:
            min1 = i
    return min1


def maximum(length):
    max1 = length[0]
    for i in length:
        if i > max1:
            max1 = i
    return max1


def average(length):
    avg = 0
    for i in length:
        avg = avg + i
    return avg / (len(length))


def moreThanAvg(length, avg):
    lst = []
    for i in length:
        if i > avg:
            lst.append(i)
    return lst

def f(length):
    min1 = minimum(length)
    max1 = maximum(length)
    avg = average(length)
    lst = moreThanAvg(length, avg)
    return min1, max1, avg, lst


minVal, maxVal, avgVal, lstAll = f(l)

print(minVal)
print(maxVal)
print(avgVal)
print(lstAll)

minVal, maxVal, avgVal, lstAll = f(l2)
print(minVal)
print(maxVal)
print(avgVal)
print(lstAll)
