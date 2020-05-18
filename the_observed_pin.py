import random


def get_pins(pin):
    adjacentDigits = {
        "1": [2, 4, 1],
        "2": [1, 3, 5, 2],
        "3": [2, 6, 3],
        "4": [1, 5, 7, 4],
        "5": [2, 4, 6, 8, 5],
        "6": [3, 5, 9, 6],
        "7": [4, 8, 7],
        "8": [5, 7, 9, 0, 8],
        "9": [8, 6, 9],
        "0": [8, 0]}
    variants = []
    possibleVariants = 1
    for i in range(len(pin)):
        possibleVariants *= len(adjacentDigits[pin[i]])

    while len(variants) != possibleVariants:
        variant = ""
        for digit in pin:
            variant += str(random.choice(adjacentDigits[digit]))
        if variant not in variants:
            variants.append(variant)

    return variants


print(get_pins("1357"))
