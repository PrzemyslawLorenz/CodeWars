import math


def isSquare(number):
    try:
        x = int(math.sqrt(number))
        if x*x == number:
            return True
        else:
            return False
    except ValueError:
        return False


print(isSquare(-1))
print(isSquare(0))
print(isSquare(3))
print(isSquare(4))
print(isSquare(25))
print(isSquare(26))
