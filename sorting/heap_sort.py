def sort(arr):
    pass


# build heap in arr
def build(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    return arr


def heapify(arr, n, i):
    '''
    heapify make sure the sub-heap
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
        heapify(arr, n, largest)
    return arr


def heap_sort(arr):
    n = len(arr)
    arr = build(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, n - 1, 0)
    return arr


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 8]
    print(f"before: {arr}")
    print(f"heapify: {build(arr)}")
    print(f"heap sort: {heap_sort(arr)}")
