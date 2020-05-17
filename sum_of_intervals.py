def sum_of_intervals(array):
    for i in range(len(array)):
        array[i] = list(array[i])
    summ = 0
    array = sorted(array, key=lambda array_entry: array_entry[0])
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j][0] < array[i][1] and array[j][0] in range(array[i][0], array[i][1]):
                if array[j][1] > array[i][1]:
                    array[i][1] = array[j][1]
                    array[j] = [0, 0]
                else:
                    array[j] = [0, 0]
    for i in range(len(array)):
        summ += array[i][1] - array[i][0]
    return summ


print(sum_of_intervals(
    [
        [1, 5],
        [10, 20],
        [1, 6],
        [16, 19],
        [5, 11]
    ]))
print(sum_of_intervals(
    [
        [1, 2],
        [6, 10],
        [11, 15]
    ]))
print(sum_of_intervals(
    [
        [1, 4],
        [7, 10],
        [3, 5]
    ]))
print(sum_of_intervals([(1, 5)]))
print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
