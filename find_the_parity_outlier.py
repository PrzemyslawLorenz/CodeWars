def find_outlier(integers):
    odd = 0
    even = 0
    for number in integers:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1

    if even > odd:
        for number in integers:
            if number % 2 != 0:
                return number
    else:
        for number in integers:
            if number % 2 == 0:
                return number


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
