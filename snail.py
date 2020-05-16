def snail(snail_map):
    road = []
    if snail_map == [[]]:
        return []
    else:
        while True:
            road.extend(snail_map[0])
            del(snail_map[0])
            if snail_map == []:
                break
            a = [[0]*len(snail_map) for i in range(len(snail_map[0]))]
            for i, x in zip(range(len(snail_map[0])), reversed(range(len(snail_map[0])))):
                for j in range(len(snail_map)):
                    a[i][j] = snail_map[j][x]
            snail_map = a

    return road


print(snail([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]))
print(snail([[1, 2, 3, 1],
             [4, 5, 6, 4],
             [7, 8, 9, 7],
             [7, 8, 9, 7]]))
print(snail([[]]))
print(snail([[1, 1, 3, 4, 5],
             [2, 5, 4, 5, 6],
             [3, 4, 5, 6, 7],
             [4, 8, 6, 7, 8],
             [7, 8, 9, 1, 2]]))
