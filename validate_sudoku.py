import math


class Sudoku(object):
    def __init__(self, data):
        # Size of Sudoku = NxN -> N = len(data)
        sS = math.sqrt(len(data))  # sS = length of small square

        # Checking data
        # Not empty and correct size ?
        if sS >= 1 and sS == int(sS):
            for i in data:
                # Square size ?
                if len(i) == len(data):
                    for j in i:
                        # Element is integer and is in range from 1 to N (N included)?
                        if type(j) == int and 1 <= j <= len(data):
                            self.data = data
                            self.sS = int(sS)
                        else:
                            return None
                else:
                    return None
        else:
            return None

    def is_valid(self):
        try:
            all = []
            # Adding lines and columns
            for x in range(len(self.data)):
                newColumn = []
                all.append(self.data[x])
                for y in range(len(self.data)):
                    newColumn.append(self.data[y][x])
                all.append(newColumn)

            # Adding small squares
            for s in range(self.sS):
                newSquare = []
                for x in range(len(self.data)):
                    newSquare.extend(
                        self.data[x][s*self.sS: s*self.sS+self.sS])
                    if len(newSquare) == 9:
                        all.append(newSquare)
                        newSquare = []

            for i in all:
                for j in i:
                    if i.count(j) > 1:
                        return False
            return True
        except AttributeError:
            return False


goodSudoku1 = Sudoku([
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]
])

goodSudoku2 = Sudoku([
    [1, 4, 2, 3],
    [3, 2, 4, 1],

    [4, 1, 3, 2],
    [2, 3, 1, 4]
])

badSudoku1 = Sudoku([
    [0, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
])

badSudoku2 = Sudoku([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1]
])

goodSudoku3 = Sudoku([[1]])
badSudoku3 = Sudoku([['j']])
badSudoku4 = Sudoku([[-1]])
badSudoku5 = Sudoku([[]])

print(goodSudoku1.is_valid())
print(goodSudoku2.is_valid())
print(badSudoku1.is_valid())
print(badSudoku2.is_valid())
print(goodSudoku3.is_valid())
print(badSudoku3.is_valid())
print(badSudoku4.is_valid())
print(badSudoku5.is_valid())
