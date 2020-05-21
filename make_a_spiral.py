def spiralize(size):
    if size < 5:
        return 0
    spiral = []
    x = size
    y = 0
    for i in range(size):
        spiral.append([0] * size)
    while x > 0:
        for i in reversed(range(y, x)):
            for j in reversed(range(y-1, x)):
                if i == y or j == x - 1 or j == y:
                    spiral[i][j] = 1
                if i == x - 1 and j > y:
                    spiral[i][j] = 1
                if i == y and j == y-1:
                    spiral[i][j] = 1
                if j == y and i == y+1:
                    spiral[i][j] = 0
        x -= 2
        y += 2

    return spiral


print(spiralize(5))
print(spiralize(10))
print(spiralize(9))
