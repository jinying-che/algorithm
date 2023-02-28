def sort(arr):
    return heap_sort(arr)


# build heap in arr
def heap(arr):
    '''
    heapify all the non-leaf nodes
    `n // 2 - 1` is the last non-leaf node in the heap (key point)
    '''
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr


def heapify(arr, n, i):
    '''
    heapify make sure the tree rooted at i is a max-heap (from top to bottom)
    - arr: input array
    - n: the length of the array
    - i: the index of the current node which is the root of the current heap
    '''
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # once swapped, heapify to make sure the child heap is a max-heap
        heapify(arr, n, largest)
    return arr


def heap_sort(arr):
    '''
    1. build a max-heap within the array
    2. swap the root (max value) with the last leaf node (pick up the largest)
    3. heapify the rest array
    3. repeatily 2 && 3 until the start of the array
    '''
    n = len(arr)
    arr = heap(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print(f"{i}, arr{arr}")
    return arr


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 8]
    print(f"before: {arr}")
    print(f"heapify: {heap(arr)}")
    print(f"heap sort: {heap_sort(arr)}")
