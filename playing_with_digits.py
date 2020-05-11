def dig_pow(n, p):
    result = 0
    for digit in str(n):
        result += int(digit) ** p
        p += 1

    if result % n == 0:
        return result / n
    else:
        return -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))
