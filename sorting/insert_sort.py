def sort(arr):
    if len(arr) <= 1:
        return arr
    length = len(arr)
    for i in range(1, length):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
    return arr
