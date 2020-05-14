def unique_in_order(iterable):
    array = []
    i = 0
    for el in iterable:
        if el not in array:
            array.append(el)
            i += 1
        if el != array[i - 1]:
            array.append(el)
            i += 1

    return array


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
