# quick sort in place

import random

def partition(arr, low, high):
    if low == high:
        return low
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    print("low: {}, high: {}, index: {}, arr: {}".format(low, high, i, arr))
    return i

def quicksort(arr, low=0, high=None):
    if high == None:
        high = len(arr)
    if low >= high:
        return arr
    index = partition(arr, low, high - 1)
    quicksort(arr, low, index)
    quicksort(arr, index + 1, high)
    return arr


if __name__ == '__main__':
    sample = random.sample(range(1,100), 10)
    print("sample: {}".format(sample))
    print(quicksort(sample))
