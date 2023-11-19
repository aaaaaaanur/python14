# a = 20, b = 24
# сложить все числа из промежутка, цифры в которые не повторяются
def summ(a, b):
    list1 = list(range(a, b + 1))
    # list1 = [20, 21, 22, 23, 24]
    sum2 = 0
    for i in list1:
        l = []
        for y in str(i):
            y2 = int(y)
            l.append(y2)
        if len(set(l)) == len(l):
            sum2 = sum2 + i
    return sum2


print(summ(20, 24))





