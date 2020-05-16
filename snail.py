def snail(arr):
    road = []
    temp = len(arr)*len(arr[0])
    if arr == [[]]:
        return road
    else:
        while(len(road) != temp):
            road.extend(arr[0])
            if(len(road) == temp):
                break
            del(arr[0])
            a = [[0]*len(arr) for i in range(len(arr[0]))]
            for i in range(len(arr[0])):
                for j in range(len(arr)):
                    a[i][j] = arr[j][i]
            
            a[0], a[-1] = a[-1], a[0]
            arr = a

    return road


print(snail([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]))
print(snail([[1, 2, 3, 1],
             [4, 5, 6, 4],
             [7, 8, 9, 7],
             [7, 8, 9, 7]]))
print(snail([[]]))
