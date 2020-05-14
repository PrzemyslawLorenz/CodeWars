def max_sequence(arr):
    if all(number < 0 for number in arr) or not arr:
        return 0

    sumList = []
    for i in range(len(arr)):
        singleSum = arr[i]
        for j in range(i + 1, len(arr)):
            singleSum += arr[j]
            sumList.append(singleSum)

    return max(sumList)


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_sequence([-1, -2, -3, -4, -5, -6, -7, -8, -9]))
print(max_sequence([]))
