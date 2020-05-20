import pprint


def spiral(size):
    if size < 5:
        return 0
    macierz = []
    x = size
    y = 0
    for i in range(size):
        macierz.append(['0'] * size)
    while x > 0:
        for i in reversed(range(y, x)):
            for j in reversed(range(x)):
                if i == x - 1 or i == y or j == x - 1 or j == 0:
                    macierz[i][j] = '1'
                if j == 0 and i == 1:
                    macierz[i][j] = '0'
        x -= 2
        y += 2
    pprint.pprint(macierz)


print(spiral(5))
print(spiral(10))
print(spiral(9))
