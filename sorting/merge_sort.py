'''
merge sort - quick implementation version
to demostate the algorithm, easy to understand

- time complexity: O(nlogn)
- space complexity: O(nlogn)
'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    return merge(left, right)


# sorting in the merge function actually
def merge(left, right):
    ret = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ret.append(left[i])
            i = i + 1
        else:
            ret.append(right[j])
            j = j + 1
    ret += left[i:]
    ret += right[j:]
    return ret


# for unit test
def sort(arr):
    return merge_sort(arr)
