def first_non_repeating_letter(string):
    for _ in range(len(string)):
        for character in string:
            if string.lower().count(character.lower()) ==  1:
                return character
    return ''


print(first_non_repeating_letter("stress"))
print(first_non_repeating_letter("sTreSS"))
print(first_non_repeating_letter("Sttress"))
print(first_non_repeating_letter("sttrreess"))
