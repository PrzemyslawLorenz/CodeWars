import math


def is_square(number):
    try:
        x = int(math.sqrt(number))
        return x**2 == number
    except ValueError:
        return False


print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))
