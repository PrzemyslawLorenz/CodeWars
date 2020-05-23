def decompose(number):
    target = number**2
    array = []
    summ = []
    x = number
    y = -1

    while sum(summ) != number**2:
        for i in reversed(range(1, x)):
            if i**2 <= target:
                array.extend([i])
                summ.extend([i**2])
                target -= i**2

        if sum(summ) != number**2:
            try:
                if array[y] == 1:
                    x = array[y-1]
                    y -= 1
                else:
                    x = array[y]
            except IndexError:
                return None
            del(array[y:])
            del(summ[y:])
            target = number**2 - sum(summ)

    return sorted(array)


print(decompose(50))
print(decompose(11))
print(decompose(5))
print(decompose(8))
print(decompose(12))
