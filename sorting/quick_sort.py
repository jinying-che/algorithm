# quick sort is divide-and-conquer algorithm
# 1. select a pivot
# 2. partition the elements into two sub-arrays (less than and greater than pivot)
# 3. the sub-array repeat 1 & 2 recursively 
# 4. add on: sort in place, no extra space needed
#
# where to test: https://leetcode.com/problems/sort-an-array/description/

import random

# for the standard solution, quick sort should sort in palce
def quicksort_in_place(arr, low, high):
    if low >= high:
        return arr
    # low and high in both functions are the exact index (e.g. low = 0, high = len(arr) -1)
    index = partition(arr, low, high)
    quicksort_in_place(arr, low, index - 1)
    quicksort_in_place(arr, index + 1, high)
    return arr

def partition(arr, low, high):
    if low == high:
        return low
    i = low
    pivot = arr[high] 

    # Improvement 1: use middle element as the pivot
    # p_index = (low + high) // 2

    # Improvement 2: use random element between low and high as pivot
    # p_index = random.randint(low, high)

    # arr[p_index], arr[high] = arr[high], arr[p_index]
    # pivot = arr[high]

    # patition in place, loop once only
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    print("low: {}, high: {}, index: {}, arr: {}".format(low, high, i, arr))
    return i

# this solution is for algorithm demostration, it needs extra space but easy to understand
def quicksort_extra_space(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) - 1]
    left = [x for x in arr if x < pivot]
    eq = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort_extra_space(left) + eq + quicksort_extra_space(right)


if __name__ == '__main__':
    sample = random.sample(range(1,100), 10)
    print("sample: {}".format(sample))

    sorted_array = quicksort_in_place(sample, 0, len(sample) - 1)
    print(f"quick sort in place: {sorted_array}")

    sorted_array = quicksort_extra_space(sample)
    print(f"quick sort in place: {sorted_array}")
