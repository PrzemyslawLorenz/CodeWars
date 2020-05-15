def find_even_index(arr):
    sumI = 0
    for i in range(len(arr)):
        sumJ = 0
        for j in reversed(range(i + 1, len(arr))):
            sumJ += arr[j]
        if sumI == sumJ:
            return i
        else:
            sumI += arr[i]
    return -1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))
print(find_even_index([1, 100, 50, -51, 1, 1]))
print(find_even_index([1, 2, 3, 4]))
