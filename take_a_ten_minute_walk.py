def is_valid_walk(walk):
    if len(walk) == 10:
        start = [0, 0]
        for direction in walk:
            if direction == 'n':
                start[0] += 1
            elif direction == 's':
                start[0] -= 1
            elif direction == 'e':
                start[1] += 1
            elif direction == 'w':
                start[1] -= 1
            else:
                return False

        if start == [0, 0]:
            return True
        else:
            return False
    else:
        return False


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk(['w']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))
