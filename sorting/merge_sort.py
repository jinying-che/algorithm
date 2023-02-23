def merge_sort(arr, low, high):
    if len(arr) <= 1:
        return arr
    mid = low + (high - low) / 2
    left = merge_sort(arr, low, mid)
    right = merge_sort(arr, mid, high)
    return merge(left, right)


def merge(left, right):
    ret = []
    left_len = len(left)
    right_len = len(right)
    i, j = 0, 0
    while i < left_len or j < right_len:
        if left[i] < left[j]:
            ret.append(left[i])
            i = i + 1
        else:
            ret.append(right[j])
            j = j + 1
    ret.append(left[i:])
    ret.append(right[i:])
    return ret
