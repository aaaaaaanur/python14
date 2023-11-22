# мяу/
# нарисовать ёлочку
#           *
#          ***
#         *****
#           |


# level * 2 - 1
# levels - level
def firtree(lev):
    for i in range(1, lev + 1):
        z = (' ' * (lev - i)) + ((i * 2 - 1) * '*')
        print(z)
    print(' ' * (lev - 1) + '|')
firtree(5)
