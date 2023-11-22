# перевернуть порядок элементов в списке a задом наперед

def rev(arr):
    b = []
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])
    return b


def rev2(arr):
    b = []
    for i in range(0, len(arr)):
        idx = len(arr) - 1 - i
        b.append(arr[idx])
    return b




a = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(rev(a))
print(rev2(a))