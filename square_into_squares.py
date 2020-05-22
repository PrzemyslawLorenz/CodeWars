def decompose(number):
    target = number**2
    array = []
    summ = []
    x = number

    while sum(summ) != number**2:
        for i in reversed(range(1, x)):
            if i**2 <= target:
                array.extend([i])
                summ.extend([i**2])
                target -= i**2

        if sum(summ) != number**2:
            try:
                x = array[1]
            except IndexError:
                return None
            target = number**2 - array[0]**2
            del(array[1:])
            del(summ[1:])

    return sorted(array)


print(decompose(50))
print(decompose(11))
print(decompose(5))
print(decompose(8))
print(decompose(12))
