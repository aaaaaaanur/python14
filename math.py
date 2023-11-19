def summ(a, b):
    if a >= b:
        return 0


    sum1 = 0
    for i in range(a, b + 1):
        if i % 2 == 0 and i % 10 != 6:
            sum1 = sum1 + i
    return sum1


print(summ(1, 36))